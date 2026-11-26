-- List score and name for rows with a non-null/non-empty name, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
