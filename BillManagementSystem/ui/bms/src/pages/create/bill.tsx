import { useSession, getSession } from "next-auth/react";
import Sidebar from "../sidebar";
import Appbar from "../appbar";
import AddBill from "../../components/Forms/add_bill";
import { Breadcrumb, Layout, Menu, theme, Space } from "antd";
import React from "react";
import { setContext } from '@apollo/client/link/context';
import client, { httpLink } from "../../apollo-client";
import { ApolloClient, InMemoryCache, gql, createHttpLink } from '@apollo/client';

export const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
};

const { Header, Sider, Content, Footer } = Layout;
const headerStyle: React.CSSProperties = {
    textAlign: 'center',
    color: '#fff',
    height: 64,
    lineHeight: '64px',
    backgroundColor: '#7dbcea',
};

const contentStyle: React.CSSProperties = {
    textAlign: 'center',
    minHeight: 120,
    lineHeight: '120px',
    color: '#fff',
    backgroundColor: '#108ee9',
};

const siderStyle: React.CSSProperties = {
    textAlign: 'center',
    lineHeight: '120px',
    color: '#fff',
    backgroundColor: '#3ba0e9',
};

const footerStyle: React.CSSProperties = {
    textAlign: 'center',
    color: '#fff',
    backgroundColor: '#7dbcea',
};

export default function bill() {
    const {
        token: { colorBgContainer },
    } = theme.useToken();
    const { data: session, status } = useSession();

    const onFinish = async (values: any) => {
        const client = new ApolloClient({
            cache: new InMemoryCache(),
            link: authLink.concat(httpLink)
        });

        console.log(values);
    
        const response = await client.mutate({
            mutation: gql`
          mutation {
            createBill(data: {
              title: "${values.title}",
              category: ${values.category},
              user: ${session?.user.id},
              amount: ${values.amount},
              note: "${values.note}"
            }) {
              id
              title
              category {
                id
                name
              }
              amount
              note
              individualSpendings {
                id
                title
                user {
                  id
                  userBirthday
                }
              }
            }
          }
          `
        });
    }

    const authLink = setContext((_, { headers }) => {
        // get the authentication token from session object
        const token = session.accessToken;
        console.log("token found: " + token);
        // return the headers to the context so httpLink can read them
        return {
            headers: {
                ...headers,
                authorization: token ? `${token}` : "",
            }
        }
    });

    if (status == "loading") {
        return (<div className="div"><p>Loading...</p></div>);
    } else if (status == "unauthenticated") {
        window.location.href = '/login';
    }
    else {
        // authenticated
        console.log(session);

        return (
            <div style={{ height: '100vh', margin: 0, padding: 0, overflow: 'hidden' }}>
                <Layout style={{ height: '100%' }}>
                    <Header style={headerStyle}>
                        <Appbar></Appbar>
                    </Header>
                    <Layout hasSider style={{ margin: 0, padding: 0 }}>
                        <Sider style={siderStyle}>
                            <Sidebar></Sidebar>
                        </Sider>
                        <Content style={contentStyle}>
                            <AddBill onFinish={onFinish}></AddBill>
                        </Content>
                    </Layout>
                    <Footer style={footerStyle}>Footer</Footer>
                </Layout>
            </div>
        );
    }
}