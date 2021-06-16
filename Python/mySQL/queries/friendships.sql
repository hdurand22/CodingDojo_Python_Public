USE friendships;

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ("Bruce", "Lee", NOW(), NOW()),
("Arnold", "Schwarzenegger", NOW(), NOW()),
("Sylvester", "Stallone", NOW(), NOW()),
("Jean-Claude", "Van Damme", NOW(), NOW()),
("Jackie", "Chan", NOW(), NOW()),
("Charlize", "Theron", NOW(), NOW());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 2, NOW(), NOW()),
(1, 4, NOW(), NOW()),
(1, 6, NOW(), NOW());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (2, 1, NOW(), NOW()),
(2, 3, NOW(), NOW()),
(2, 5, NOW(), NOW());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (3, 2, NOW(), NOW()),
(3, 5, NOW(), NOW());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (4, 3, NOW(), NOW());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (5, 1, NOW(), NOW()),
(5, 6, NOW(), NOW());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (6, 2, NOW(), NOW()),
(6, 3, NOW(), NOW());

SELECT users.first_name, users.last_name, friends.first_name, friends.last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as friends ON friendships.friend_id = friends.id;

SELECT users.first_name, users.last_name, friends.first_name, friends.last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as friends ON friendships.friend_id = friends.id
WHERE users.id = 1;

SELECT COUNT(friend_id) FROM friendships;

SELECT users.first_name, users.last_name, friends.first_name, friends.last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as friends ON friendships.friend_id = friends.id
WHERE users.id = 3
ORDER BY friends.last_name;

