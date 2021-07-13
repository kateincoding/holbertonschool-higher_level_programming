-- script that lists all records of a table second_table
-- database hbtn_0c_0 in your MySQL server
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC, name;
