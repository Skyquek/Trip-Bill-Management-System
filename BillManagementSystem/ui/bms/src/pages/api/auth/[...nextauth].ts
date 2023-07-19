import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider  from "next-auth/providers/credentials";
import client from "../../../apollo-client";
import { gql } from "@apollo/client";
import { getLogger } from "../../../logging/log-util";

type loginCredentials = {
  username: string;
  password: string;
};

// For more information on each option (and a full list of options) go to
// https://next-auth.js.org/configuration/options
export const authOptions: NextAuthOptions = {

  // https://next-auth.js.org/configuration/providers/oauth
  providers: [
    CredentialsProvider({
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
              "username": data.tokenAuth.user.username,
              "email": data.tokenAuth.user.email
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
  // callbacks: {
  //   async jwt({ token }) {
  //     console.log("jwt callback");
  //     console.log(token.email);
  //     return token
  //   },
  // },
}

export default NextAuth(authOptions)