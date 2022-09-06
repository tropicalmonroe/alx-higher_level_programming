-- list the no of rec with the same score the tbl of the db in your MySQL server
-- ecords are ordered by descending count
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
