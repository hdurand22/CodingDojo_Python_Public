USE books;

INSERT INTO authors (first_name, last_name, created_at, updated_at)
VALUES ("Jane", "Austen", NOW(), NOW()),
("Emily", "Dickinson", NOW(), NOW()),
("Fyodor", "Dostoevsky", NOW(), NOW()),
("William", "Shakespeare", NOW(), NOW()),
("Lao", "Tzu", NOW(), NOW());

INSERT INTO books (title, created_at, updated_at)
VALUES ("C Sharp", NOW(), NOW()),
("Java", NOW(), NOW()),
("Python", NOW(), NOW()),
("PHP", NOW(), NOW()),
("Ruby", NOW(), NOW());

UPDATE books SET title = "C#", updated_at = NOW() 
WHERE id = 1;

UPDATE authors SET first_name = "Bill", updated_at = NOW()
WHERE id = 4;

INSERT INTO favorites (author_id, book_id, created_at, updated_at)
VALUES (1, 1, NOW(), NOW()),
(1, 2, NOW(), NOW());

INSERT INTO favorites (author_id, book_id, created_at, updated_at)
VALUES (2, 1, NOW(), NOW()),
(2, 2, NOW(), NOW()),
(2, 3, NOW(), NOW());

INSERT INTO favorites (author_id, book_id, created_at, updated_at)
VALUES (3, 1, NOW(), NOW()),
(3, 2, NOW(), NOW()),
(3, 3, NOW(), NOW()),
(3, 4, NOW(), NOW());

INSERT INTO favorites (author_id, book_id, created_at, updated_at)
VALUES (4, 1, NOW(), NOW()),
(4, 2, NOW(), NOW()),
(4, 3, NOW(), NOW()),
(4, 4, NOW(), NOW()),
(4, 5, NOW(), NOW());

SELECT authors.first_name, authors.last_name, books.title
FROM authors
JOIN favorites ON authors.id = favorites.author_id
LEFT JOIN books ON books.id = favorites.book_id
WHERE books.id = 3;

INSERT INTO favorites (author_id, book_id, created_at, updated_at)
VALUES (5, 2, NOW(), NOW());

SELECT authors.first_name, authors.last_name, books.title
FROM authors
JOIN favorites ON authors.id = favorites.author_id
JOIN books ON books.id = favorites.book_id
WHERE books.id = 5;




 


