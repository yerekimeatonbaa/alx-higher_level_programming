-- A script that creates a Mysql server user user_0d_1
-- user user_0d_1 should have priviledges on the server
-- password should be set to user_0d_1_pwd

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
