BEGIN;
--
-- Create model Bill
--
CREATE TABLE "accounting_bill" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "title" varchar(50) NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "category_id" bigint NOT NULL REFERENCES "accounting_category" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model IndividualSpending
--
CREATE TABLE "accounting_individualspending" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "bill_id" bigint NOT NULL REFERENCES "accounting_bill" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Remove field user from payment
--
CREATE TABLE "new__accounting_payment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL);
INSERT INTO "new__accounting_payment" ("id", "created", "modified", "amount_currency", "amount", "note") SELECT "id", "created", "modified", "amount_currency", "amount", "note" FROM "accounting_payment";
DROP TABLE "accounting_payment";
ALTER TABLE "new__accounting_payment" RENAME TO "accounting_payment";
CREATE INDEX "accounting_bill_category_id_9a361127" ON "accounting_bill" ("category_id");
CREATE INDEX "accounting_individualspending_bill_id_849dc932" ON "accounting_individualspending" ("bill_id");
--
-- Rename model Student to User
--
ALTER TABLE "accounting_student" RENAME TO "accounting_user";
--
-- Delete model Expenses
--
DROP TABLE "accounting_expenses";
--
-- Delete model Payment
--
DROP TABLE "accounting_payment";
--
-- Add field user to individualspending
--
CREATE TABLE "new__accounting_individualspending" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "bill_id" bigint NOT NULL REFERENCES "accounting_bill" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "accounting_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__accounting_individualspending" ("id", "created", "modified", "amount_currency", "amount", "note", "bill_id", "user_id") SELECT "id", "created", "modified", "amount_currency", "amount", "note", "bill_id", NULL FROM "accounting_individualspending";
DROP TABLE "accounting_individualspending";
ALTER TABLE "new__accounting_individualspending" RENAME TO "accounting_individualspending";
CREATE INDEX "accounting_individualspending_bill_id_849dc932" ON "accounting_individualspending" ("bill_id");
CREATE INDEX "accounting_individualspending_user_id_03313e8f" ON "accounting_individualspending" ("user_id");
--
-- Add field user to bill
--
CREATE TABLE "new__accounting_bill" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "modified" datetime NOT NULL, "title" varchar(50) NOT NULL, "amount_currency" varchar(3) NOT NULL, "amount" decimal NOT NULL, "note" text NOT NULL, "category_id" bigint NOT NULL REFERENCES "accounting_category" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "accounting_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__accounting_bill" ("id", "created", "modified", "title", "amount_currency", "amount", "note", "category_id", "user_id") SELECT "id", "created", "modified", "title", "amount_currency", "amount", "note", "category_id", NULL FROM "accounting_bill";
DROP TABLE "accounting_bill";
ALTER TABLE "new__accounting_bill" RENAME TO "accounting_bill";
CREATE INDEX "accounting_bill_category_id_9a361127" ON "accounting_bill" ("category_id");
CREATE INDEX "accounting_bill_user_id_4c56d681" ON "accounting_bill" ("user_id");
COMMIT;
