
from pymongo import MongoClient
import pandas as pd

# Connection string
connection_string = "mongodb+srv://techvaseegrah:kL5RvAyrOQBVFQAc@cluster0.pbjj6kp.mongodb.net/F3-DB?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(connection_string)

# Select the database
db = client["F3-RE"]

# Select the collections
orders_collection = db.orders
products_collection = db.products
customers_collection = db.customers

# Define the fields to retrieve for orders
orders_fields = {
    "customer_id": 1,
    "line_items.product_id": 1,
    "line_items.name": 1,
    "_id": 0  # Exclude the default _id field
}

# Define the fields to retrieve for products
products_fields = {
    "categories.id": 1,
    "categories.name": 1,
    "name": 1,
    "_id": 0  # Exclude the default _id field
}

# Define the fields to retrieve for customers
customers_fields = {
    "id": 1,
    "_id": 0  # Exclude the default _id field
}

# Fetch the data
orders_data = list(orders_collection.find({}, orders_fields))
products_data = list(products_collection.find({}, products_fields))
customers_data = list(customers_collection.find({}, customers_fields))

# Convert to Pandas DataFrames
orders_df = pd.DataFrame(orders_data)
products_df = pd.DataFrame(products_data)
customers_df = pd.DataFrame(customers_data)

# Print the DataFrames
print("\nOrders DataFrame:")
print(orders_df)

print("\nProducts DataFrame:")
print(products_df)

print("\nCustomers DataFrame:")
print(customers_df)
