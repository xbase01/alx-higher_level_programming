-- Creates the database hbtn_0d_2 if it doesn't already exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Creates the user user_0d_2 with the SELECT privilege on hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grants SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
