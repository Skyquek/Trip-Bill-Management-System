import Sidebar from "../sidebar";
import Appbar from "../appbar";
import { Breadcrumb, Layout, Menu, theme, Space } from "antd";
import React from "react";
import AddCategory from "../../components/Forms/add_category";

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

export default function category() {
    const {
        token: { colorBgContainer },
    } = theme.useToken();

    return (
        <div style={{ height: '100vh', margin: 0, padding:0, overflow: 'hidden' }}>
            <Layout style={{height: '100%' }}>
                <Header style={headerStyle}>
                    <Appbar></Appbar>
                </Header>
                <Layout hasSider style={{ margin:0, padding: 0 }}>
                    <Sider style={siderStyle}>
                        <Sidebar></Sidebar>
                    </Sider>
                    <Content style={contentStyle}>
                        <AddCategory></AddCategory>
                    </Content>
                </Layout>
                <Footer style={footerStyle}>Footer</Footer>
            </Layout>
        </div>
    );
}