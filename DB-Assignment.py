from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Decimal
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)
    products = relationship('Product', back_populates='category')
    product_inventories = relationship('ProductInventory', back_populates='category')

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    deleted_at = Column(DateTime)
    category = relationship('ProductCategory', back_populates='products')
    product_inventory = relationship('ProductInventory', back_populates='product')

class ProductInventory(Base):
    __tablename__ = 'product_inventory'
    id = Column(Integer, primary_key=True)
    SKU = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    created_at = Column(DateTime)
    inventory_id = Column(Integer, ForeignKey('product_inventory.id'))
    modified_at = Column(DateTime)
    price = Column(Decimal)
    deleted_at = Column(DateTime)
    product = relationship('Product', back_populates='product_inventory')

class Discount(Base):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    desc = Column(Text)
    discount_percent = Column(Decimal, nullable=False)
    active = Column(Boolean, nullable=False)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)