import React from 'react';
import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Checkbox, Form, Input } from 'antd';
import { signIn } from 'next-auth/react';
import { redirect } from 'next/navigation';
import { useSession, signOut } from 'next-auth/react';
import { Card } from 'antd';

const App: React.FC = () => {
  const {data: session, status} = useSession();

  const onFinish = async (values: any) => {
    // use nextAuth API
    const result = await signIn('credentials', { 
      redirect: false,
      username: values.username,
      password: values.password,
    });

    if (session !== undefined || null) {
      console.log(session);
    }
  };

  function logoutHandler() {
    signOut();
  }

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' , height: '100vh'}}>
      <Card style={{ width: 300 }}>
        <Form
          name="normal_login"
          className="login-form"
          initialValues={{ remember: true }}
          onFinish={onFinish}
        >
          <Form.Item
            name="username"
            rules={[{ required: true, message: 'Please input your Username!' }]}
          >
            <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" />
          </Form.Item>
          <Form.Item
            name="password"
            rules={[{ required: true, message: 'Please input your Password!' }]}
          >
            <Input
              prefix={<LockOutlined className="site-form-item-icon" />}
              type="password"
              placeholder="Password"
            />
          </Form.Item>
          <Form.Item>
            <Form.Item name="remember" valuePropName="checked" noStyle>
              <Checkbox>Remember me</Checkbox>
            </Form.Item>

            <a className="login-form-forgot" href="">
              Forgot password
            </a>
          </Form.Item>

          <Form.Item>
            <Button type="primary" htmlType="submit" className="login-form-button">
              Log in
            </Button>
            Or <a href="">register now!</a>
          </Form.Item>
        </Form>
      </Card>
      

      {/* {
      status === 'authenticated' ? <Button onClick={logoutHandler}>LogOut</Button> : null
      // status === 'authenticated' ? window.location.href = '/create/bill' : null
      }       */}
    </div>
  );
};

export default App;