USE twitter;

INSERT INTO users (first_name, last_name, handle, birthday, created_at, updated_at) 
VALUES ("James", "Harden", "JHarden13", '1989-08-26', NOW(), NOW());

SELECT first_name, last_name FROM users
WHERE id > 2;

UPDATE users SET handle = "thefakeJamesHarden", updated_at = NOW()
WHERE id = 8; 

DELETE FROM users WHERE id > 6;