# Bill Management System (BMS)

This project originated from a problem I faced while on vacation with friends. During one of my recent trips, we encountered difficulties in keeping track of who paid for which bills, resulting in confusion and uneven expenses where some individuals paid for certain items while others paid for others.

## Problems

Ali, Ah Chong, and Mei Mei went on a vacation in Kuala Lumpur. For breakfast, Ali spent RM 10, Ah Chong spent RM 14, and Mei Mei spent RM 6. Mei Mei helped pay for the bill, which came to a total of RM 30.

Later that night, they had dinner at a fancy restaurant. Ali's meal cost RM 35, Ah Chong's cost RM 30, and Mei Mei's cost RM 100. Ali paid for the bill, which came to a total of RM 165.

When they settled the bills, Ali didn't owe anything. Ah Chong owed Mei Mei RM 14 and Ali RM 30. Mei Mei owed Ali RM 90 (RM 100 minus the RM 10 she contributed to the breakfast bill).

## Solution

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
    user ||--o{ friendship : "is"
    user ||--o{ group: "involved"
    user ||--o{ expense_split : "is involved in"

    user {
        string id PK "UUID"
        string username "username"
        string password "password"
        string name
        string email
        string phone_number
        string currency "All MYR, only support MYR for now"
        string language "For emails and notifications"
        string profile_picture "path to system storage"
    }
    friendship {
        string id PK "uuid"
        int user1_id "user 1 id"
        int user2_id "user 2 id"
    }
    
    group {
        string id PK "uuid"
        string name "group name"
        string group_picture "group photo (optional)"
        enum type "trip, home, couple, other"
        datetime start "event start date"
        datetime end "event end date"
    }
    expense ||--|{ expense_split : "is involved in"
    expense ||--|| group: "is spending in"
    expense {
        string id PK "uuid"
        string category "category of the spending"
        string name "name of the expense"
        decimal amount "amount spend in this expense"
        string group FK "which group does this expense belong to"
        datetime date "when is this expense being created?"
        string image "image of receipt (optional)"
        string note "some note to indicate or record somethings (optional)"
    }
    split_method ||--|{ expense_split : "specifies"
    split_method {
        string id PK "uuid"
        string name "how to split (equally, unequally)"
        string description "the description of each splitting technique"
    }
    
    expense_split {
        string id PK "uuid"
        string expense_id  FK
        string user_id FK
        string split_method_id FK
    }

    user ||--o{ comment : "can post"
    group ||--o{ comment : "can contain"

    comment {
        string id PK "uuid"
        string user_id FK "which user"
        string group_id FK "what is this suer comment"
    }

    debt {
        string id PK "uuid"
        string debtor_user_id FK "who is the borrower? the lazy to pay one."
        string creditor_user_id FK "who paid for the expense? The good guy."
        decimal amount "Positive: owes, Negative: is owed"
    }

    user ||--o{ debt : "can owe"
    user ||--o{ debt : "can be owed"

```
