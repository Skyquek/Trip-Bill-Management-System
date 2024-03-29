import React, { useEffect, useState } from 'react';
import { Button, Form, Input, InputNumber, Select } from 'antd';
import type { FormInstance } from 'antd/es/form';
import axios from 'axios';
import { gql } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';
import client from "../../apollo-client";
import { useSession } from 'next-auth/react';
import { onFinishFailed } from '@/pages/create/bill';

const { Option } = Select;

export default function AddBill({onFinish}) {
  const [categories, setCategories] = useState<{id: string; name: string}[]>([]);
  useEffect(() => {
    fetchCategories();
  }, []);

  async function fetchCategories() {
    const { data } = await client.query({
      query: gql`
      query {
          category {
            id
            name
          }
        }
      `,
    });

    setCategories(data.category);
  }

    console.log('pass');

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
        label="Title"
        name="title"
        rules={[{ required: true, message: 'Please input title for your bill!' }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Category"
        name="category"
        rules={[{ required: true, message: 'What is the category for this bill?' }]}
      >
        <Select
          placeholder="Select bill category here!"
          allowClear
        >
          {categories.map((category) => (
            <Option key={category.id} value={category.id}>
              {category.name}
            </Option>
          ))}
        </Select>
      </Form.Item>

      <Form.Item
        label="Amount"
        name="amount"
        rules={[{ required: true, message: 'What is the amount for this bill?' }]}
      >
        <InputNumber />
      </Form.Item>

      <Form.Item
        name="note"
        label="Note"
        rules={[{ required: false, message: 'Any note?' }]}
      >
        <Input.TextArea showCount maxLength={100} />
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};