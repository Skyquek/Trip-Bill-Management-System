import { ApolloClient, InMemoryCache } from '@apollo/client';
import { gql, createHttpLink } from '@apollo/client';

const client = new ApolloClient({
    uri: "http://127.0.0.1:8000/graphql/",
    cache: new InMemoryCache()
});

export const httpLink = createHttpLink({
    uri: 'http://127.0.0.1:8000/graphql/',
});

export default client;