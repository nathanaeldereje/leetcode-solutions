SELECT player_id, event_date AS first_login
FROM (
    SELECT player_id, event_date,
           ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
    FROM Activity
) t
WHERE rn = 1;

