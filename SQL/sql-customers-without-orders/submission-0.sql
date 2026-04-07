-- Write your query below

-- Given two tables, customers and orders. 
-- customers: id (Pk), name
-- orders: id(Pk), cust_id(fk - customers)

-- Show all customers who never placed an order
-- project the name from the customer table on the condition
--  their ids are not present in orders table

select customers.name from 
customers left join orders on (customers.id = orders.customer_id)
where orders.customer_id is NULL;