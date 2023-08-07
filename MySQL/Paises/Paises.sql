/*¿Qué consulta ejecutarías para obtener todos los países que hablan esloveno? Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  
Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente.*/
SELECT countries.name AS 'País', language.language AS 'Idioma', language.percentage AS 'Porcentaje de habla'
FROM countries 
JOIN languages language ON countries.id = language.country_id
WHERE language = 'Slovene'
ORDER BY language.percentage DESC;

/*¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  
Tu consulta debe devolver el nombre del país, el idioma y el número total de ciudades. 
Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente.*/

SELECT countries.name AS 'País', COUNT(cities.id) AS 'Número de ciudades'
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.id) DESC;

/*¿Qué consulta ejecutarías para obtener todos ciudades de México con una población mayor a 500,000?
 Tu consulta debe ordenar el resultado por población en orden descendente.*/
 
SELECT name AS 'Ciudad', population AS 'Población', cities.country_id
FROM cities
WHERE country_id = (SELECT id FROM countries WHERE name = 'Mexico')
AND population > 500000
ORDER BY population DESC;
 
 /*¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%? 
 Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente.*/
 
SELECT countries.name AS 'País', language.language AS 'Idioma', language.percentage AS 'Porcentaje de habla'
FROM countries
JOIN languages language ON countries.id = language.country_id
WHERE language.percentage > 89
ORDER BY language.percentage DESC;

/*¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 
y población mayor a 100,000?*/

SELECT name AS 'País', surface_area AS 'Área de superficie', population AS 'Población'
FROM countries
WHERE surface_area < 501 AND population > 100000;

/*¿Qué consulta ejecutarías para obtener países solo con monarquía constitucional, 
un capital superior a 200 y una esperanza de vida mayor a 75 años?*/

SELECT name AS 'País', government_form AS 'Monarquía constitucional', capital AS 'Capital', life_expectancy AS 'Esperanza de vida'
FROM countries
WHERE government_form ='Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

/*¿Qué consulta ejecutarías para obtener todas las ciudades de Argentina dentro del distrito 
de Buenos Aires con una población mayor a 500,000 habitantes? La consulta debe devolver 
el nombre del país, el nombre de la ciudad, el distrito y la población.*/

SELECT countries.name AS 'País', cities.name AS 'Ciudad', cities.district AS 'Distrito', cities.population AS 'Población'
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;

/*¿Qué consulta ejecutarías para resumir el número de países en cada región? Tu consulta debe 
mostrar el nombre de la región y el número de países. Además, debe ordenar el resultado por el 
número de países en orden descendente.*/

SELECT region AS 'Región', COUNT(countries.id) AS 'Número de países'
FROM countries
GROUP BY region
ORDER BY COUNT(countries.id) DESC;
