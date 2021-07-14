-- script that creates the database hbtn_0d_usa and the table cities
-- id must be a foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL);
