import React, { useEffect, useState } from 'react';
import { Button, Form, Input, InputNumber, Select } from 'antd';
import type { FormInstance } from 'antd/es/form';
import axios from 'axios';

const { Option } = Select;

export default function AddCategory() {

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  const onFinish = async (values: any) => {

    try {
      const response = await axios.post('http://127.0.0.1:8000/graphql/', {
        query: `
        mutation {
            createCategory(data: {
                  name: "${values.categoryName}"
              }) {
                      id
                      name
              }
          }
        `,
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log(response.data); 
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Form
      name="basic"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      style={{ maxWidth: 600 }}
      initialValues={{ remember: true }}
      autoComplete="off"
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
    >
      <Form.Item
        label="Category Name"
        name="categoryName"
        rules={[{ required: true, message: 'Please input your new cool category!' }]}
      >
        <Input />
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};