USE users;

INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ("Hayden", "Durand", "hayden@hayden.com", NOW(), NOW()),
("Mom", "Durand", "mom@mom.com", NOW(), NOW()),
("Dad", "Durand", "dad@dad.com", NOW(), NOW());

SELECT * FROM users;

SELECT * FROM users 
WHERE email = "hayden@hayden.com";

SELECT * FROM users
WHERE id = 3;

UPDATE users SET last_name = "Pancakes", updated_at = NOW()
WHERE id = 3;

DELETE FROM users
WHERE id = 2;

SELECT * FROM USERS
ORDER BY first_name;

SELECT * FROM USERS
ORDER BY first_name DESC;