/* 1.-Consulta: crea 3 usuarios nuevos*/
INSERT INTO usuario (nombre, apellido, email)
VALUES ( 'Felipe', 'Del Solar', 'felipe@delsolar.com'),
	   ( 'Ana Maria', 'Reveco', 'ana@reveco.com' ),
	   ( 'Paz', 'Del Solar', 'paz@delsolar.com' );

SELECT * FROM usuario;

/*2.-Recupera el primer usuario usando su dirección de correo electrónico*/
SELECT * FROM usuario
WHERE email = 'felipe@delsolar.com';

/*3.-Recupera el último usuario usando su id*/
/*4.-Consulta: cambia el usuario con id=3 para que su apellido sea Panqueques*/
SELECT * FROM usuario
WHERE id = 3;

UPDATE usuario SET apellido = "Panqueques"
WHERE usuario.id = 3;

/*5.-Elimina el usuario con id=2 de la base de datos*/
DELETE FROM usuario
WHERE usuario.id = 2;

/*6.-Obtén todos los usuarios, ordenados por su nombre */
SELECT * FROM usuario
ORDER BY nombre;

/*Consulta BONUS: obtén todos los usuarios, ordenados por su nombre en orden descendente*/
SELECT * FROM usuario
ORDER BY nombre DESC;

