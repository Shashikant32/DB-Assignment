CREATE TABLE product_category (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  desc TEXT,
  created_at TIMESTAMP,
  modified_at TIMESTAMP,
  deleted_at TIMESTAMP
);

CREATE TABLE product (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  category_id INT,
  deleted_at TIMESTAMP,
  FOREIGN KEY (category_id) REFERENCES product_category(id)
);

CREATE TABLE product_inventory (
  id INT PRIMARY KEY,
  SKU VARCHAR(255) NOT NULL,
  quantity INT NOT NULL,
  category_id INT,
  created_at TIMESTAMP,
  inventory_id INT,
  modified_at TIMESTAMP,
  price DECIMAL,
  deleted_at TIMESTAMP,
  FOREIGN KEY (category_id) REFERENCES product_category(id),
  FOREIGN KEY (inventory_id) REFERENCES product_inventory(id)
);

CREATE TABLE discount (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  desc TEXT,
  discount_percent DECIMAL NOT NULL,
  active BOOLEAN NOT NULL,
  created_at TIMESTAMP,
  modified_at TIMESTAMP,
  deleted_at TIMESTAMP
);