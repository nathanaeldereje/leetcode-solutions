WITH combDept AS (
    SELECT 
        d.name AS department,
        e.name AS employee,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Employee e
    LEFT JOIN Department d ON e.departmentId = d.id
)
SELECT department, employee, salary
FROM combDept
WHERE salary_rank <= 3;

