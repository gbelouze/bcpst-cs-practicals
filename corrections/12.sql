-- 1a
SELECT Name, Capital FROM country;

-- 1b
SELECT * FROM country;

-- 2a
SELECT Name, Population
    FROM country
    ORDER BY Population DESC
    LIMIT 3;

-- 2b
SELECT Name
    FROM country
    ORDER BY Population ASC
    LIMIT 2
    OFFSET 3

-- 3a
SELECT c.Name
    FROM country as c JOIN encompasses as e ON c.Code = e.Country
    WHERE (e.continent = "South America" OR e.continent = "North America")
        AND Population / Area < 10;
        -- attention, sans le parenthèsage, AND a priorité sur OR

-- 3b
-- on ne pouvait pas la faire car on a besoin de la table city qui n'est pas présentée
-- mais si on avait su que la table city contenait une colonne Country que est une clef
-- étrangère pour country.Code, voilà ce qu'on aurait écrit
SELECT city.Name
    FROM country
        JOIN encompasses ON country.Code = encompasses.Country
        JOIN city ON country.Code = city.Country
    WHERE encompasses.Continent = "Europe"
        AND city.latitude > 60
        AND city.Name = country.Capital;

-- 3c
SELECT c.Name, c.Area * e.Percentage
    FROM country as c JOIN encompasses as e ON c.Code = e.Country
    WHERE e.continent = "Asia" AND c.Area * e.Percentage > 1000000
    ORDER BY c.Area * e.Percentage DESC;

-- 4a
SELECT SUM(c.Area * e.Percentage)
    FROM country as c JOIN encompasses as e ON c.Code = e.Country
    WHERE e.continent = "Africa";

-- 4b
SELECT SUM(Population) FROM country;

-- 4c
SELECT AVG(Population) FROM country;

-- 4d
SELECT COUNT(*) FROM country WHERE Area > 1000000;
