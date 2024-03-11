# DB-Assignment
# This appears to be a database schema for an e-commerce product catalog.

# The schema includes several tables:

# 1. 'product_category':
This table contains information about different categories of products, with columns for the category ID (integer), name (varchar), description (text), creation time (timestamp), and last modification time (timestamp). It also includes a 'deleted_at' timestamp, suggesting that categories can be marked as deleted without being permanently removed.
# 2. 'product': 
This table contains information about individual products, with columns for the product ID (integer), name (varchar), and 'deleted_at' timestamp.
# 3. 'product_inventory': 
This table contains information about the inventory of each product, with columns for the inventory ID (integer), SKU (varchar), quantity (integer), category ID (integer), creation time (timestamp), inventory ID (integer), last modification time (timestamp), price (decimal), and discount ID (integer).
# 4. 'discount':
This table contains information about discounts that can be applied to products, with columns for the discount ID (integer), name (varchar), description (text), discount percentage (decimal), active status (boolean), creation time (timestamp), and last modification time (timestamp). It also includes a 'deleted_at' timestamp.
