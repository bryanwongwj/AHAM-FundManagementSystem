DELETE FROM "public"."funds" WHERE id = '1';
DELETE FROM "public"."funds" WHERE id = '2';
DELETE FROM "public"."funds" WHERE id = '3';

DELETE FROM "public"."fund_managers" WHERE id = '1';
DELETE FROM "public"."fund_managers" WHERE id = '2';
DELETE FROM "public"."fund_managers" WHERE id = '3';

INSERT INTO "public"."fund_managers" ("id", "name") VALUES ('1', 'bryanwongwj');
INSERT INTO "public"."fund_managers" ("id", "name") VALUES ('2', 'estherteo');
INSERT INTO "public"."fund_managers" ("id", "name") VALUES ('3', 'johndoe');

INSERT INTO "public"."funds" ("id", "name", "fund_manager_id", "dscp", "nav", "dt_create", "performance") VALUES ('1', 'TestFund1', '1', 'First fund for testing', '1.2253', '2024-11-09 08:57:31', '150.545364');
INSERT INTO "public"."funds" ("id", "name", "fund_manager_id", "dscp", "nav", "dt_create", "performance") VALUES ('2', 'AHAM Enhanced Deposit Fund', '2', 'The Fund aims to provide Investors with a regular income stream and high level of liquidity to meet cash flow requirement whilst maintaining capital preservation.', '1.2253', '2024-11-09 13:48:07', '183.644138');
INSERT INTO "public"."funds" ("id", "name", "fund_manager_id", "dscp", "nav", "dt_create", "performance") VALUES ('3', 'AHAM Select Bond Fund', '2', 'To provide investors with a steady income stream over the medium to long-term period through investments primarily in bonds and other fixed income securities.', '0.5808', '2024-11-09 13:59:34', '254.612278');

SELECT setval('fund_managers_id_seq', 3, TRUE);
SELECT setval('funds_id_seq', 3, TRUE);