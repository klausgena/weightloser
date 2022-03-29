-- create users

INSERT INTO users(name, password, reg_date, sex, kg, cm, age, activity, target)
VALUES ('Nicolas', 'nicolas', '15-03-2022', 'm', 97, 183, 47, 2, 500);
INSERT INTO users(name, password, reg_date, sex, kg, cm, age, activity, target)
VALUES ('Maria', 'maria', '15-03-2022', 'f', 60, 161, 62, 1, 500);
INSERT INTO users(name, password, reg_date, sex, kg, cm, age, activity, target)
VALUES ('Joelik', 'joeli', '15-03-2022', 'm', 89, 170, 30, 2, 500);

-- log some data

INSERT INTO weights(weight, date, user_id)
VALUES (96.9, '16-03-2022', 1);
INSERT INTO weights(weight, date, user_id)
VALUES (61, '16-03-2022', 2);
INSERT INTO weights(weight, date, user_id)
VALUES (88, '16-03-2022', 3);

INSERT INTO calories(logging, date, user_id)
VALUES (1, '16-03-2022', 1);
INSERT INTO calories(logging, date, user_id)
VALUES (2, '16-03-2022', 1);
INSERT INTO calories(logging, date, user_id)
VALUES (3, '16-03-2022', 1);
