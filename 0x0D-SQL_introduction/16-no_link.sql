-- display all records starting with score and name in descending order
SELECT score, name FROM second_table HAVING name IS NOT NULL ORDER BY score DESC;
