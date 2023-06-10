-- Creates the database 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Creates the table 'cities' in the 'hbtn_0d_usa' database if it doesn't already exist
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`state_id`) REFERENCES `hbtn_0d_usa`.`states` (`id`)
);
