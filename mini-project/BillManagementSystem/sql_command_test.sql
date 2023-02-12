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
CREATE TABLE "accountings_payment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "user_id_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Expenses
--
CREATE TABLE "accountings_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "category_id" bigint NOT NULL REFERENCES "accountings_category" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Debt
--
CREATE TABLE "accountings_debt" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "user_id_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "accountings_payment_user_id_id_8398c27b" ON "accountings_payment" ("user_id_id");
CREATE INDEX "accountings_expenses_category_id_54df5b5f" ON "accountings_expenses" ("category_id");
CREATE INDEX "accountings_expenses_user_id_id_1fa9b981" ON "accountings_expenses" ("user_id_id");
CREATE INDEX "accountings_debt_user_id_id_2edd167f" ON "accountings_debt" ("user_id_id");
COMMIT;
