# Bill Management System (BMS)

This project originated from a problem I faced while on vacation with friends. During one of my recent trips, we encountered difficulties in keeping track of who paid for which bills, resulting in confusion and uneven expenses where some individuals paid for certain items while others paid for others.

## Problems:

Ali, Ah Chong, and Mei Mei went on a vacation in Kuala Lumpur. For breakfast, Ali spent RM 10, Ah Chong spent RM 14, and Mei Mei spent RM 6. Mei Mei helped pay for the bill, which came to a total of RM 30.

Later that night, they had dinner at a fancy restaurant. Ali's meal cost RM 35, Ah Chong's cost RM 30, and Mei Mei's cost RM 100. Ali paid for the bill, which came to a total of RM 165.

When they settled the bills, Ali didn't owe anything. Ah Chong owed Mei Mei RM 14 and Ali RM 30. Mei Mei owed Ali RM 90 (RM 100 minus the RM 10 she contributed to the breakfast bill).

## Solution:

The BMS system resolved the issue by displaying to each user the amount owed to or by other participants for the entirety of the trip.

## Home Bill Management System

```mermaid
flowchart LR
    id1[[Login]] --> id2[[Add Payment]]
    --> id3[/Input bills/] --> id4[/Add Note/]
    --> id5[/Input payer name/] --> id6[/Input individual cost/]
    --> id7[[Click View Debt]] --> id8[/Display Debt Summary/]
``` 

### ERD

```mermaid
erDiagram
    user ||--o{ bill : pay
    user {
        int id PK
        string username
        string password
        string name
        date birthdate
        string email
        string phone_number
    }

    bill }o--|| category: "has"
    bill {
        int id PK
        string category FK "Category of Spending"
        int user_id FK "Which user pay for this?"
        varchar title
        decimal amount
        string note
        datetime created
        datetime modified
    }

    individual_spending }|--|| bill: "has"
    individual_spending {
        int id PK
        int bill_id FK
        int user_id FK
        decimal amount "Amount of each user spending"
        datetime created
        datetime modified
    }

    category {
        int id PK
        string name
    }
```

Note: 

```
Tax = (bill_amount - SUM(individual_spending)) / len(individual_spending)
```


TODO LIST:

Create:

- [x] Category
- [ ] User
- [ ] Bill
- [ ] Individual User

Read:
- [x] Category
- [ ] User
- [x] Bill
- [ ] Individual User

Update:

Delete:
