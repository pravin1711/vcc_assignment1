CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO students (roll_number, name, email) VALUES
('101', 'Alice Johnson', 'alice@example.com'),
('102', 'Bob Smith', 'bob@example.com');
