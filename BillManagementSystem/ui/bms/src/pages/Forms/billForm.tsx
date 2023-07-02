import React, { useEffect, useState } from 'react';
import { Button, Form, Input, InputNumber, Select } from 'antd';
import type { FormInstance } from 'antd/es/form';
import axios from 'axios';

const { Option } = Select;

export default function BillForm() {
  const [categories, setCategories] = useState<{id: string; name: string}[]>([]);
  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = () => {
    axios.post('http://127.0.0.1:8000/graphql/', {
      query: `
        query {
          category {
            id
            name
          }
        }
      `,
    })
    .then((response) => {
      const categoryData = response.data.data.category;
      
      // We want to perform side effect here
      setCategories(categoryData);
    })
    .catch((error) => {
      console.error(error);
    })
  }

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  const onFinish = async (values: any) => {

    try {
      const response = await axios.post('http://127.0.0.1:8000/graphql/', {
        query: `
          mutation {
            createBill(data: {
              title: "${values.title}",
              categoryId: 3,
              userId: 1,
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