-- script that lists all records of the table of db in mysqlserver
-- desc order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
