-- Creates the table force_name with id and name if it doesn't already exist
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT,
    `name` VARCHAR(256) NOT NULL
);
