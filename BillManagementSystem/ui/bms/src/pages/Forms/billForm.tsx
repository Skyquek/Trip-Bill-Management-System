import React from 'react';
import { Button, Checkbox, Form, Input, InputNumber, Select } from 'antd';
import type { FormInstance } from 'antd/es/form';

const { Option } = Select;

const BillForm: React.FC = () => {
  const formRef = React.useRef<FormInstance>(null);

  const onCategoryChange = (value: string) => {
    switch (value) {
      case 'male':
        formRef.current?.setFieldsValue({ note: 'Hi, man!' });
        break;
      case 'female':
        formRef.current?.setFieldsValue({ note: 'Hi, lady!' });
        break;
      case 'other':
        formRef.current?.setFieldsValue({ note: 'Hi there!' });
        break;
      default:
        break;
    }
  };

  const onFinish = (values: any) => {
    console.log(values);
  };

  const onReset = () => {
    formRef.current?.resetFields();
  };

  const onFill = () => {
    formRef.current?.setFieldsValue({ note: 'Hello world!', gender: 'male' });
  };

  return (
  <Form
    name="basic"
    labelCol={{ span: 8 }}
    wrapperCol={{ span: 16 }}
    style={{ maxWidth: 600 }}
    initialValues={{ remember: true }}
    autoComplete="off"
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
      rules={[{ required: true, message: 'What is the category for this bills?' }]}
    >
      <Select
        placeholder="Select a option and change input text above"
        onChange={onCategoryChange}
        allowClear
      >
        <Option value="male">Food</Option>
        <Option value="female">Parking</Option>
        <Option value="other">Commute</Option>
      </Select>
    </Form.Item>

    <Form.Item
    label="Amount"
    name="amount"
    rules={[{ required: true, message: 'What is the amount for this bills?' }]}
    >
     <InputNumber /> 
    </Form.Item>

    <Form.Item
        name="note"
        label="note"
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

export default BillForm;