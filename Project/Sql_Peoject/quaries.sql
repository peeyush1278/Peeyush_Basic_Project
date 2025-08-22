SELECT *
FROM rentals
WHERE rental_date >= CURDATE() - INTERVAL 30 DAY;
SELECT payment_method, COUNT(*) AS count, 
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM payment), 2) AS percentage
FROM payment
GROUP BY payment_method;
SELECT r.customer_id, AVG(p.amount) AS avg_revenue
FROM rentals r
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY r.customer_id
ORDER BY avg_revenue DESC;
SELECT DATE_FORMAT(payment_date, '%Y-%m') AS yaer_month,
       SUM(amount) AS total_revenue
FROM payment
GROUP BY yaer_month
ORDER BY yaer_month;
SELECT movie_id, title
FROM movies
WHERE movie_id NOT IN (
    SELECT DISTINCT movie_id FROM rentals
);
SELECT m.genre, COUNT(*) AS total_rentals
FROM rentals r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY m.genre
ORDER BY total_rentals DESC;
SELECT movie_id, COUNT(*) AS times_rented
FROM rentals
GROUP BY movie_id
ORDER BY times_rented DESC
LIMIT 5;
SELECT DISTINCT customer_id
FROM rentals
WHERE rental_status = 'Overdue';
SELECT customer_id, COUNT(*) AS rental_count
FROM rentals
GROUP BY customer_id
ORDER BY rental_count DESC
LIMIT 10;
SELECT customer_id, COUNT(*) AS total_rentals
FROM rentals
GROUP BY customer_id
ORDER BY total_rentals DESC;
select Customers.name, count(*) as total_rental
from Customers,rentals
group by Customers.name;