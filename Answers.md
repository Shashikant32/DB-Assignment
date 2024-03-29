# Q1. Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.
# Answer:= 
From the above diagram, we can see that the "Product" entity has a foreign key category_id which references the id of the "Product_Category" entity. This indicates a one-to-many relationship between "Product_Category" and "Product", where a single product category can have multiple products associated with it.
# Q2. How could you ensure that each product in the "Product" table has a valid category assigned to it?
# Answer:= 
To ensure that each product in the "Product" table has a valid category assigned to it, you could implement a constraint on the category_id column of the "Product" table. This constraint would ensure that any attempt to insert a new product into the table without a valid category_id would result in an error. Additionally, you could enforce this constraint at the application level by ensuring that a valid category is always selected or provided when creating a new product.
