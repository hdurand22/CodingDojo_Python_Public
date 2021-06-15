USE dojos_and_ninjas_schema;

INSERT INTO dojos (name, created_at, updated_at) 
VALUES ("Bellevue", NOW(), NOW()),
("San Jose", NOW(), NOW()),
("Chicago", NOW(), NOW());

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

INSERT INTO dojos (name, created_at, updated_at) 
VALUES ("Los Angeles", NOW(), NOW()),
("Boston", NOW(), NOW()),
("New York City", NOW(), NOW());

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Hayden", "Durand", 28, NOW(), NOW(), 4),
("David", "Bowie", 69, NOW(), NOW(), 4),
("Stevie", "Wonder", 71, NOW(), NOW(), 4);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Tupac", "Shakur", 25, NOW(), NOW(), 5),
("Christopher", "Wallace", 25, NOW(), NOW(), 5),
("Shawn", "Carter", 51, NOW(), NOW(), 5);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Linda", "Ronstadt", 74, NOW(), NOW(), 6),
("Lady", "Gaga", 35, NOW(), NOW(), 6),
("Dolly", "Parton", 75, NOW(), NOW(), 6);

SELECT * FROM ninjas WHERE dojo_id = 4;
SELECT * FROM ninjas WHERE dojo_id = 6;
SELECT * FROM ninjas WHERE id=(SELECT max(id) FROM ninjas);
