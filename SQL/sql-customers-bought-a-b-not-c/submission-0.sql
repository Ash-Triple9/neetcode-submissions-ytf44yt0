-- Write your query below

-- Show ordered customer id and customer name
-- conditions: 
    -- buys two products A and B but not a third product C

-- What we can do is first:
-- selecting a table with ids from customers buying both A and B
-- except
-- selecting a table with ids from customers who have bought C

-- should give us ids of customers who haven't bought C yet but bought A and B

select customer_id, customer_name from 
(
    select customer_id, customer_name from
    (
        select c.customer_id, c.customer_name from
            customers c join orders o on c.customer_id = o.customer_id
            where o.product_name = 'A'
        intersect
        select c.customer_id, c.customer_name from
            customers c join orders o on c.customer_id = o.customer_id
            where o.product_name = 'B'
    ) c
    except
    select c.customer_id, c.customer_name from
    customers c join orders o on c.customer_id = o.customer_id
    where o.product_name = 'C'
) d order by d.customer_name;