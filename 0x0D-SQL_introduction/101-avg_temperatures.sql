-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending
-- display table
SELECT city, AVG(value)
AS avg_temp
FROM temperatures
    GROUP BY city ORDER BY avg_temp DESC;
