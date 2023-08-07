INSERT INTO usuarios( nombre, apellido, email, contraseña )
VALUES ( 'Alex', 'Miller', 'alex@miller.com', 'pass1234');

DELETE FROM usuarios 
WHERE id = 1;

SELECT *
FROM usuarios;

SELECT *
FROM recetas;

SELECT *
FROM recetas r JOIN usuarios u
	ON  r.id_usuario = u.id;