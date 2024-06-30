
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

# Fetch the data
orders_data = list(orders_collection.find({}, orders_fields))

# Convert to Pandas DataFrame
orders_df = pd.DataFrame(orders_data)

# Print the Orders DataFrame
print("\nOrders DataFrame:")
print(orders_df)

# Normalize the line_items to flatten the DataFrame
orders_df = orders_df.explode('line_items')

# Remove rows with NaN values in line_items
orders_df = orders_df.dropna(subset=['line_items'])

# Extract product_id and name from line_items
orders_df['product_id'] = orders_df['line_items'].apply(lambda x: x['product_id'] if isinstance(x, dict) else None)
orders_df['product_name'] = orders_df['line_items'].apply(lambda x: x['name'] if isinstance(x, dict) else None)

# Remove rows with NaN values in product_id and product_name
orders_df = orders_df.dropna(subset=['product_id', 'product_name'])

# Group by product_id and product_name to count the occurrences
top_selling_products = orders_df.groupby(['product_id', 'product_name']).size().reset_index(name='count')

# Sort by count in descending order and get the top 3 products
top_three_products = top_selling_products.sort_values(by='count', ascending=False).head(3)

# Print the top three most selling products
print("\nTop Three Most Selling Products:")
print(top_three_products)
