-- Write your query below

-- Given a table customers where id and year are PKs
-- Need to find customers who had positive revenue in the year 2020.
-- Two conditions:
--  revenue > 0, year = 2020 these can go in our where condition
--  project customer_id from the customer table

select customer_id from customers 
where revenue>0 and year = 2020