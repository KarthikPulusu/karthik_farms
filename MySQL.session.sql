CREATE DATABASE karthikfarms;

USE karthikfarms;

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    number BIGINT,
    address TEXT,
    pincode INT,
    gender ENUM('male', 'female', 'others'),
    item VARCHAR(50),
    quantity VARCHAR(20),
    transaction_id VARCHAR(100)
);
