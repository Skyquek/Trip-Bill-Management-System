import React, { useEffect, useState } from 'react';
import { Button, Form, Input, InputNumber, Select } from 'antd';
import type { FormInstance } from 'antd/es/form';
import axios from 'axios';
import { gql } from '@apollo/client';
import client from '@/apollo-client';

const { Option } = Select;

export default function AddCategory() {

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  const onFinish = async (values: any) => {

    const { data } = await client.mutate({
      mutation: gql`
        mutation {
          createCategory(data: {
                name: "${values.categoryName}"
            }) {
                    id
                    name
          }
        }
      `,
    });

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