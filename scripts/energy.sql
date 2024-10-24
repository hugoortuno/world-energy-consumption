CREATE DATABASE IF NOT EXISTS `energy`;


SELECT *
FROM `energy`.`energy_data` AS e
JOIN (
    SELECT Region AS `Región`, LifeExpectancy AS `Expectativa de vida`, Code
    FROM world.country
) AS w ON e.`Código ISO` = w.`Code`
JOIN (
    SELECT name_es AS `País ES`, continent_es AS Continente, km2 AS `Superficie, km2`, code_3 
    FROM energy.country_info_raw
) AS c ON e.`Código ISO` = c.code_3;