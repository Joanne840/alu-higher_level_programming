-- Create table unique_id with default id = 1 and UNIQUE constraint
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
