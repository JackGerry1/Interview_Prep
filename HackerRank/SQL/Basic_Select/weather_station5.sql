/*
Enter your query here.
*/

SELECT city, LENGTH(city) as city_length FROM station ORDER BY city_length asc, city LIMIT 1;
SELECT city, LENGTH(city) as city_length FROM station ORDER BY city_length desc, city LIMIT 1;

