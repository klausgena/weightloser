DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS weights;
DROP TABLE IF EXISTS calories;

CREATE TABLE users(
       id INTEGER PRIMARY KEY NOT NULL,
       name VARCHAR(30) UNIQUE NOT NULL,
       password VARCHAR NOT NULL,
       reg_date TEXT NOT NULL,
       sex INTEGER NOT NULL,
       kg REAL NOT NULL,
       cm INTEGER NOT NULL,
       age INTEGER NOT NULL,
       activity INTEGER NOT NULL,
       target INTEGER NOT NULL,
       CHECK(activity < 6)
       );
CREATE TABLE weights(
       weight REAL NOT NULL,
       date TEXT NOT NULL,
       user_id INTEGER NOT NULL,
       FOREIGN KEY(user_id) REFERENCES users(id)
       );
CREATE TABLE calories(
       logging INTEGER NOT NULL DEFAULT 0,
       date TEXT NOT NULL,
       user_id INTEGER NOT NULL,
       FOREIGN KEY(user_id) REFERENCES users(id)
       );
       
