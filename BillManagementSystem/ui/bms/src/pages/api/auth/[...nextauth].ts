import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider  from "next-auth/providers/credentials";
import client from "../../../apollo-client";
import { gql } from "@apollo/client";
import { getLogger } from "../../../logging/log-util";
import jwt from "jsonwebtoken";
import chalk from "chalk";

// For more information on each option (and a full list of options) go to
// https://next-auth.js.org/configuration/options
export const authOptions: NextAuthOptions = {

  // https://next-auth.js.org/configuration/providers/oauth
  providers: [
    CredentialsProvider({
      // How to delete this? I have my own signin page.
      name: "Credentials (Deprecated)",
      credentials: {
        username: { label: "Username", type: "text", placeholder: "jsmith" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        // Add logic here to look up the user from the credentials supplied        
        if (credentials?.username === undefined || credentials?.password === undefined) { 
          return null;
        } else {
          let username = credentials.username;
          let password = credentials.password;

          // let username = "new_user4";
          // let password = "SuperSecureP@sw0rd";

          const { data } = await client.mutate({
            mutation: gql`
            mutation {
              tokenAuth(username: "${username}", password: "${password}") {
                success
                errors
                refreshToken {token created revoked expiresAt isExpired __typename}
                token {
                  payload {
                    origIat
                    exp
                  }
                  token
                }
                user {
                  isActive
                  username
                  email
                  status {
                    verified
                  }
                }
              }
            }  
            `,
          });

          // console.log(data.tokenAuth.success);
          if (data.tokenAuth.success === true) {
            // Any object returned will be saved in `user` property of the JWT
            const user = {
              "serverRefreshToken": data.tokenAuth.refreshToken.token,
              "isActive": data.tokenAuth.user.isActive,
              "name": data.tokenAuth.user.username,
              "email": data.tokenAuth.user.email,
              "accessToken": data.tokenAuth.token.token,
            }
            return user;
          } else {
            // console.log('error lel');
            // console.error(data);
             // If you return null then an error will be displayed advising the user to check their details.
            //  return Error('Could not log you in.');
            return null;
             // You can also Reject this callback with an Error thus the user will be sent to the error page with the error message as a query parameter
          }
        }
      }
    })
  ],
  callbacks: {
    async jwt({ account, token, user, profile }) {
      const data = {...token};

      if (user && user.accessToken) {
        console.log(user.accessToken);
        data.email = user.email;
        data.name = user.name;
        data.accessToken = user.accessToken;

        return data;
      }

      const payload = jwt.decode(data.accessToken, { json: true });
      if (!payload) {
        console.error(chalk.red('AccessToken after 2nd call is invalid:', data));
        throw new Error('Unable to decode');
      }
      // const { exp, id } = payload;

      // if (exp && id) {
      //   const timeEpoch = exp * 1000; // seconds to milliseconds
      //   if (dayjs(timeEpoch).isBefore(new Date())) {
      //     // refresh
      //     console.log(chalk.yellow('should refresh token'));
      //     const {
      //       data: { accessToken },
      //     } = await refreshAccessToken( . . . );
      //     data.accessToken = accessToken; // currently not work...
      //   }
      // }

      return data;
    },
    async session({ session, user, token, newSession, trigger }) {
      const alteredSession = { ...session };
      if (alteredSession.user != undefined) {
        alteredSession.user.name = token.name;
        alteredSession.user.email = token.email;
      }
      
      // This will be returned to the client so be careful what to send here.
      return {
        ...alteredSession,
        accessToken: token.accessToken,
      };
    },
  },
}

export default NextAuth(authOptions)