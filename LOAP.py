from pymongo import MongoClient
import pandas as pd

# Connection string
connection_string = "mongodb+srv://techvaseegrah:kL5RvAyrOQBVFQAc@cluster0.pbjj6kp.mongodb.net/F3-DB?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(connection_string)

# Select the database
db = client["F3-RE"]

# Select the products collection
products_collection = db.products

# Define the fields to retrieve for products
products_fields = {
    "categories.id": 1,
    "categories.name": 1,
    "name": 1,
    "_id": 0  # Exclude the default _id field
}

# Fetch the products data
products_data = list(products_collection.find({}, products_fields))

# Convert to Pandas DataFrame
products_df = pd.DataFrame(products_data)

# Set display options to show all rows
pd.set_option('display.max_rows', None)

# Print the Products DataFrame
print("\nProducts DataFrame:")
print(products_df)