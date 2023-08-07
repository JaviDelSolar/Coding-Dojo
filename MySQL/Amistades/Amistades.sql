/*Crea 6 usuarios nuevos*/
INSERT INTO usuarios( nombre, apellido )
VALUES ('María', 'Lopez'),
	   ('Laura', 'Zamora'),
       ('Pedro', 'Carmona'),
       ('Sofía', 'Suarez'),
       ('Alejandro', 'Venegas'),
       ('Paula', 'Mardonez');
SELECT * FROM usuarios;

/*Haz que el usuario 1 sea amigo del usuario 2, 4 y 6
/*Haz que el usuario 2 sea amigo del usuario 1, 3 y 5
Haz que el usuario 3 sea amigo del usuario 2 y 5
Haz que el usuario 4 sea amigo del usuario 3
Haz que el usuario 5 sea amigo del usuario 1 y 6
Haz que el usuario 6 sea amigo del usuario 2 y 3*/

INSERT INTO amistades(usuario_id, amigo_id1)
VALUES(1, 2), (1, 4), (1, 6),
	  (2, 1), (2, 3), (2, 5),
      (3, 2), (3,5),
      (4,3),
      (5,1), (5,6),
      (6,2), (6,3);
      
SELECT * FROM amistades;

SELECT * FROM usuarios
JOIN amistades ON usuarios.id=amistades.usuario_id
LEFT JOIN usuarios AS usuarios2 ON usuarios2.id = amistades.amigo_id1;

/*Devuelve todos los usuarios que son amigos del primer usuario, 
asegúrate de que sus nombres se muestren en los resultados.*/

SELECT usuarios.nombre, usuarios.apellido, usuarios2.nombre AS amigo_nombre, usuarios2.apellido AS amigo_apellido FROM usuarios
JOIN amistades ON usuarios.id = amistades.usuario_id
LEFT JOIN usuarios as usuarios2 ON usuarios2.id = amistades.amigo_id1;

SELECT usuarios2.nombre AS nombre, usuarios2.apellido AS apellido, usuarios.nombre AS amigos_con FROM usuarios
JOIN amistades ON usuarios.id = amistades.usuario_id
LEFT JOIN usuarios as usuarios2 ON usuarios2.id = amistades.amigo_id1;

SELECT COUNT(*) AS numero_de_amistades from amistades;
SELECT usuario_id, usuarios.nombre, usuarios.apellido, count(usuario_id) AS numero_de_amistades from amistades
JOIN usuarios ON usuarios.id = amistades.usuario_id
GROUP BY usuario_id
ORDER BY numero_de_amistades DESC
LIMIT 1;

SELECT usuarios2.nombre AS nombre, usuarios2.apellido AS apellido, usuarios.nombre AS amigos_con FROM usuarios
JOIN amistades ON usuarios.id = amistades.usuario_id
LEFT JOIN usuarios AS usuarios2 ON usuarios2.id = amistades.amigo_id1
WHERE usuarios.id = 3
ORDER BY nombre;
