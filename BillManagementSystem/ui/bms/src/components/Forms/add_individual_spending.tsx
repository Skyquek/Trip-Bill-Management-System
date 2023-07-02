import React, { useEffect, useState } from 'react';
import { Button, Form, Input, InputNumber, Select } from 'antd';
import type { FormInstance } from 'antd/es/form';
import axios from 'axios';

const { Option } = Select;

export default function AddIndividualSpending() {
  const [bills, setBills] = useState<any>([]);
  useEffect(() => {
    fetchBills();
  }, []);

  const fetchBills = () => {
    axios.post('http://127.0.0.1:8000/graphql/', {
        query: `
            query {
                bill {
                    id
                    title
                    note
                    amount
                    category {
                        id
                        name
                    }
                    user {
                        id
                    }
                    individualSpendings {
                        id
                        note
                        title
                        user {
                            id
                            userBirthday
                        }
                    }
                }
          }
        `,
    })
    .then((response) => {
        const bills = response.data.data.bill;
        setBills(bills)
    })
    .catch((error) => {
        console.error(error);
    });
  }

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  const onFinish = async (values: any) => {

    try {
      const response = await axios.post('http://127.0.0.1:8000/graphql/', {
        query: `
            mutation {
                createIndividualSpending(data: {
                    billId: ${values.billId},
                    userId: 1,
                    amount: ${values.amount},
                    note: "${values.note}",
                    title: "Pork Leg rice lunch"
                }) {
                        id
                        bill {
                            id
                            user {
                                id
                                userBirthday
                            }
                            title
                            category {
                                id
                                name
                            }
                            amount
                            note
                        }
                        user {
                            id
                            userBirthday
                            phoneNumber
                            bills {
                                id
                            }
                            individualSpendings {
                                id
                                title
                            }
                        }
                        amount
                        note
                        title
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
        label="Bill"
        name="billId"
        rules={[{ required: true, message: 'What is the bill Id?' }]}
      >
        <Select
          placeholder="Select bill category here!"
          allowClear
        >
          {bills.map((bill) => (
            <Option key={bill.id} value={bill.id}>
              Name: {bill.title}, Amount: {bill.amount}
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