-- Write your query below

-- We have to calculate the bonus of an employee
-- Conditions for getting said bonus:
    -- the id has to be an odd number
    -- the name has to begin with any other letter than M
-- If both conditions are met, then bonus is 100%(double) of salary, else 0

-- select id, salary as bonus if id is an odd number and name not like 'M*'

-- show id, bonus where bonus = salary if id is odd and name does not begin with M else 0

select employee_id, (case when name not like 'M%' and employee_id%2 = 1 then salary else 0 end) as bonus from employees order by employee_id;