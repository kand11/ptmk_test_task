SELECT
       full_name
     , birth_date
     , sex
FROM employees
GROUP BY full_name, birth_date, sex
ORDER BY full_name
;