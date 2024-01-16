# Bill Management System (BMS)

This project originated from a problem I faced while on vacation with friends. During one of my recent trips, we encountered difficulties in keeping track of who paid for which bills, resulting in confusion and uneven expenses where some individuals paid for certain items while others paid for others.

## Problems

Ali, Ah Chong, and Mei Mei went on a vacation in Kuala Lumpur. For breakfast, Ali spent RM 10, Ah Chong spent RM 14, and Mei Mei spent RM 6. Mei Mei helped pay for the bill, which came to a total of RM 30.

Later that night, they had dinner at a fancy restaurant. Ali's meal cost RM 35, Ah Chong's cost RM 30, and Mei Mei's cost RM 100. Ali paid for the bill, which came to a total of RM 165.

When they settled the bills, Ali didn't owe anything. Ah Chong owed Mei Mei RM 14 and Ali RM 30. Mei Mei owed Ali RM 90 (RM 100 minus the RM 10 she contributed to the breakfast bill).

## Solution

The BMS system resolved the issue by displaying to each user the amount owed to or by other participants for the entirety of the trip.

### ERD

```mermaid
erDiagram
    django_user ||--o{ friendship : "is"
    django_user ||--o{ group: "involved"
    django_user ||--|| profile: "also is"

    django_user {
       string id PK "django default"
       string username "django default"
       string first_name "django default"
       string last_name "django default"
       string email "django default"
       string is_staff "django default"
       string is_active "django default" 
       datetime date_joined "django default"
    }

    profile {
        string id PK "UUID"
        string django_user_id FK "django_user_id"
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

    debt {
        string id PK "uuid"
        string debtor_user_id FK "who is the borrower? the lazy to pay one."
        string creditor_user_id FK "who paid for the expense? The good guy."
        decimal amount "Positive: owes, Negative: is owed"
    }

    django_user ||--o{ debt : "can owe"
    django_user ||--o{ debt : "can be owed"
    
    group {
        string id PK "uuid"
        string name "group name"
        string group_picture "group photo (optional)"
        enum group_type "trip, home, couple, other"
    }
    expense ||--|| group: "is spending in"
    expense {
        string id PK "uuid"
        string group FK "which group does this expense belong to"
        string category "category of the spending"
        string name "name of the expense"
        decimal amount "amount spend in this expense"
        datetime created_at "when is this expense being created?"
        datetime updated_at "when is this expense being updated?"
        string receipt_image "image of receipt (optional)"
        string note "some note to indicate or record somethings (optional)"
    }

    django_user ||--o{ comment : "can post"
    group ||--o{ comment : "can contain"

    comment {
        string id PK "uuid"
        string user_id FK "which user"
        string expense_id "what expense is this?"
        string text "what is this user comment"
    }
```

## DJango App

1. User App:
    - Models:
        - User: Extends the default Django User model.
    - Relations:
        - Friendship: Represents a friendship relationship between users.
        - ExpenseSplit: Represents a user's involvement in splitting an expense.
        - Comment: Represents user comments.
        - Debt: Represents debts owed between users.

2. Group App:
    - Models: Group
    - Relations: User (through friendship), Expense, Comment

3. Expense App:
    - Models: Expense, SplitMethod, ExpenseSplit
    - Relations: User (through ExpenseSplit), Group (through Expense)

4. Comment App:
    - Models: Comment

5. Debt App:
    - Models: Debt

## References

1. <https://medium.com/@russell.cecala/full-stack-with-flutter-and-django-rest-framework-16fd666d39b> Get started with django rest framework.
