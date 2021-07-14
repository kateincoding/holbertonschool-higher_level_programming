-- script that creates the table unique_id on your MySQL server
-- unique id
CREATE DATABASE hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE states (
    id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL);
