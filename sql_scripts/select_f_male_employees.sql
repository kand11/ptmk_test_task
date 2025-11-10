SELECT
       full_name
     , birth_date
     , sex
FROM employees
WHERE full_name LIKE 'F%'
  AND sex = 'male';