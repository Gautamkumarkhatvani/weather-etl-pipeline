SELECT * FROM weather_data;
-- Average Temperature Per City
SELECT city, AVG(temperature) AS avg_temperature
FROM weather_data
GROUP BY city;
-- Average Humidity
SELECT city, AVG(humidity) AS avg_humidity
FROM weather_data
GROUP BY city;
-- Most Common Weather Condition
SELECT weather_condition, COUNT(*) AS frequency
FROM weather_data
GROUP BY weather_condition
ORDER BY frequency DESC;
-- Hottest Temperature Recorded
SELECT city, MAX(temperature) AS hottest_temp
FROM weather_data
GROUP BY city;
-- Coldest Temperature Recorded
SELECT city, MIN(temperature) AS coldest_temp
FROM weather_data
GROUP BY city;
-- Latest Records
SELECT *
FROM weather_data
ORDER BY recorded_at DESC
LIMIT 10;