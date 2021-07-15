-- Displays max temperature of each state
-- Query to show
SELECT state, MAX(value) AS max_temp
    FROM temperatures GROUP BY state ORDER BY state ASC;
