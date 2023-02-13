BEGIN;
--
-- Create model Category
--
CREATE TABLE "accountings_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" text NOT NULL);
--
-- Create model Student
--
CREATE TABLE "accountings_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "birthday" datetime NOT NULL, "email" varchar(254) NOT NULL, "phone_number" varchar(128) NOT NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Payment
--
CREATE TABLE "accountings_payment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Expenses
--
CREATE TABLE "accountings_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "category_id" bigint NOT NULL REFERENCES "accountings_category" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Debt
--
CREATE TABLE "accountings_debt" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "accountings_payment_user_id_4bf7fddd" ON "accountings_payment" ("user_id");
CREATE INDEX "accountings_expenses_category_id_54df5b5f" ON "accountings_expenses" ("category_id");
CREATE INDEX "accountings_expenses_user_id_be3ff88f" ON "accountings_expenses" ("user_id");
CREATE INDEX "accountings_debt_user_id_7d84dd2d" ON "accountings_debt" ("user_id");
COMMIT;
