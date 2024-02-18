-- Write a script that creates database hbtn_0d_2 & the user user_0d_2
-- User should have only SELECT privilege in the database
-- User password set to user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
FLUSH PRIVILEGES;
