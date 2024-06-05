-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS SS_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'SS_DEV'@'localhost' IDENTIFIED BY 'SS_4232o5$MM.';

-- Grant all privileges on SS_db to SS_DEV
GRANT ALL PRIVILEGES ON SS_db.* TO 'SS_DEV'@'localhost';

-- Grant SELECT privilege on performance_schema to SS_DEV
GRANT SELECT ON performance_schema.* TO 'SS_DEV'@'localhost';

