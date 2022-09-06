-- a script that lists all records in the table of the db in your MySQL server
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
