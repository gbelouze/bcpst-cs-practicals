------ Requêtes de base

-- pays de plus de 60M d'habitants
SELECT name FROM Country WHERE population > 60000000;

-- pareil trié par ordre alphabétique
SELECT name FROM Country WHERE population > 60000000 ORDER BY name ASC;

-- pays, population par ordre croissant de population
SELECT name, population FROM Country ORDER BY population ASC;

-- 10 pays de plus petite superficie
SELECT name FROM Country ORDER BY area ASC LIMIT 10;

-- les 10 suivants
SELECT name FROM Country ORDER BY area ASC LIMIT 10 OFFSET 10;


----- Jointures

-- pays à cheval sur plusieurs continent
SELECT DISTINCT c.name
    FROM Country AS c JOIN Encompasses AS e ON c.code = e.country
    WHERE e.percentage < 100;

-- les pays d'Amerique qui comptent moins de 10 habitants par km2
SELECT c.name
	FROM Country AS c JOIN Encompasses AS e ON c.code = e.country
    WHERE (e.continent = 'North America' OR e.continent = 'South America') AND c.population / c.area < 10;


-- les capitales européennes de latitude > 60deg
SELECT c.name
	FROM City AS c JOIN Encompasses AS e ON c.country = e.country
    WHERE c.latitude > 60 AND e.continent = "Europe";



----- Agrégations

-- 10 langues parlées dans le plus de pays différents
SELECT language
    FROM Spoken 
    GROUP BY language
    ORDER BY Count(*) DESC
    LIMIT 10;

-- langues parlées dans exactement 6 pays
SELECT language
    FROM Spoken GROUP BY language
    HAVING Count(*) = 6;

-- et les pays correspondant
SELECT s.language, c.name
    FROM 
        Spoken as s 
        JOIN (SELECT language FROM Spoken GROUP BY language HAVING Count(*) = 6) as g ON s.language = g.language
        JOIN Country as c ON s.country = c.code
    ORDER BY s.language ASC;

-- langues parlées par <30 000 personnes
SELECT s.language
    FROM Spoken as s
        JOIN Country as c
        ON s.country = c.code
    GROUP BY s.language
    HAVING SUM(c.population * s.percentage)/100 < 30000;


-- 5 langues les plus parlées en Afrique
SELECT s.language, FLOOR(SUM(c.population * s.percentage) / 100) as locuteurs
    FROM Spoken as s
        JOIN Country as c ON s.country = c.code
        JOIN Encompasses AS e ON e.country = c.code
    WHERE e.continent = "Africa"
    GROUP BY s.language
    ORDER BY locuteurs DESC
    LIMIT 5;


------ Sous-requêtes

-- Pays dont le taux de chomâge est inférieur à la moyenne
SELECT c.name
    FROM Country as c
        JOIN Economy as e
        ON c.code = e.country
    WHERE e.unemployment < (
        SELECT AVG(unemployment) FROM Economy
    )
        AND e.agriculture > e.industry
        AND e.agriculture > e.service;

-- Le taux d'inflation le plus faible parmi les pays industriels, pour chaque continent
SELECT en.continent, c.name
    FROM country as c
        JOIN economy as e ON c.code = e.country
        JOIN encompasses as en ON en.country = c.code
    WHERE e.industry > e.agriculture 
        AND e.industry > e.service
        AND (en.continent, e.inflation) in (
            SELECT en.continent, MIN(e.inflation)
                FROM economy as e JOIN encompasses as en ON e.country = en.country
                WHERE e.industry > e.agriculture AND e.industry > e.service
                GROUP BY en.continent
            )
