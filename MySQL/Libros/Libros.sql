/* Crea 5 usuarios diferentes: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu */
INSERT INTO usuarios (Nombre)
VALUES ('Jane Austen'), 
       ('Emily Dickinson'), 
       ('Fyodor Dostoevsky'), 
       ('William Shakespeare'), 
       ('Lau Tzu');
SELECT * FROM usuarios;

/* Crea 5 libros con los siguientes nombres: C Sharp, Java, Python, PHP, Ruby */
INSERT INTO libros (Titulo, num_paginas)
VALUES ('C Sharp', 100), 
       ('Java', 100), 
       ('Python', 100), 
       ('PHP', 100), 
       ('Ruby', 100);
SELECT * FROM libros;

/* Cambia el nombre del libro de C Sharp a C# */
UPDATE libros SET Titulo = 'C#' WHERE id = 1;
SELECT * FROM libros;

/* Cambia el nombre del cuarto usuario a Bill Shakespeare */
UPDATE usuarios SET Nombre = 'Bill Shakespeare' WHERE id = 4;
SELECT * FROM usuarios;

/* Haz que el primer usuario marque como favoritos los 2 primeros libros */
INSERT INTO favoritos (Usuario_id, Libro_id)
VALUES (4,5);
SELECT * FROM favoritos;

/*Recupera todos los usuarios que marcaron como favorito el tercer libro*/
SELECT * FROM libros
JOIN favoritos ON libros.id = favoritos.libro_id
JOIN usuarios ON usuarios.id = favoritos.usuario_id
WHERE libros.id = 3;

/*Elimina el primer usuario de los favoritos del tercer libro*/
DELETE FROM favoritos
WHERE libro_id = 3
AND usuario_id = 2;

/*Haz que el quinto usuario marque como favorito el segundo libro*/
INSERT INTO favoritos (usuario_id, libro_id)
VALUES (5,2);

/*Encuentra todos los libros que el tercer usuario marcó como favoritos*/
SELECT usuario_id from favoritos WHERE libro_id = 3 ORDER BY usuario_id LIMIT 1;

/*Encuentra todos los usuarios que marcaron como favorito el quinto libro*/
SELECT * FROM usuarios
JOIN favoritos ON usuarios.id = favoritos.usuario_id
JOIN libros ON libros.id = favoritos.libro_id
WHERE usuarios.id = 5;

SELECT * FROM libros