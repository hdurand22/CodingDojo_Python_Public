USE world;

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON country_code = countries.code
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.name) AS count
FROM countries
JOIN cities ON country_code = countries.code
GROUP BY countries.name
ORDER BY count DESC;

SELECT cities.name, cities.population
FROM cities
JOIN countries ON code = cities.country_code
WHERE cities.population > 500000 AND countries.name = "Mexico"
ORDER BY cities.population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON country_code = countries.code
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT countries.name
FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT countries.name
FROM countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON country_code = countries.code
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT region, COUNT(name) as countries
FROM countries
GROUP BY region
ORDER BY countries DESC;