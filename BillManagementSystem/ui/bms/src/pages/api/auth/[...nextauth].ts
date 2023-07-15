import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider  from "next-auth/providers/credentials";
import client from "../../../apollo-client";
import { gql } from "@apollo/client";

type loginCredentials = {
  username: string;
  password: string;
};

const login = async (values: loginCredentials) => {
  console.log(values);
  const { data } = await client.mutate({
      mutation: gql`
      mutation {
          login(username: "${values.username}", password: "${values.password}") {
              id
              username
              email
          }
      }
      `,
  });
  console.log(data.login);

  return data.login;
};

// For more information on each option (and a full list of options) go to
// https://next-auth.js.org/configuration/options
export const authOptions: NextAuthOptions = {
  // https://next-auth.js.org/configuration/providers/oauth
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        username: { label: "Username", type: "text", placeholder: "jsmith" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials, req) {
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
                login(username: "${username}", password: "${password}") {
                    id
                    username
                    email
                }
            }
            `,
          });

          if (data !== undefined) {
            console.log(data.login);

            // Any object returned will be saved in `user` property of the JWT
            return data.login;
          } else {
             // If you return null then an error will be displayed advising the user to check their details.
             return null;
             // You can also Reject this callback with an Error thus the user will be sent to the error page with the error message as a query parameter
          }
        }
      }
    })
  ],
  callbacks: {
    async jwt({ token }) {
      console.log("jwt callback");
      console.log(token.email);
      return token
    },
  },
}

export default NextAuth(authOptions)