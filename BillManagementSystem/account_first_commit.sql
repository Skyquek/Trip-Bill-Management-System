BEGIN;
--
-- Create model Category
--
CREATE TABLE "accounting_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" text NOT NULL);
--
-- Create model Student
--
CREATE TABLE "accounting_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "birthday" date NOT NULL, "phone_number" varchar(128) NOT NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Payment
--
CREATE TABLE "accounting_payment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Expenses
--
CREATE TABLE "accounting_expenses" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "category_id" bigint NOT NULL REFERENCES "accounting_category" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Debt
--
CREATE TABLE "accounting_debt" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "accounting_payment_user_id_26ec0f2f" ON "accounting_payment" ("user_id");
CREATE INDEX "accounting_expenses_category_id_ef0dee42" ON "accounting_expenses" ("category_id");
CREATE INDEX "accounting_expenses_user_id_d4a1d63a" ON "accounting_expenses" ("user_id");
CREATE INDEX "accounting_debt_user_id_ab8fbc56" ON "accounting_debt" ("user_id");
COMMIT;
