import pandas as pd
from pymongo import MongoClient

# Connection string
connection_string = "mongodb+srv://techvaseegrah:kL5RvAyrOQBVFQAc@cluster0.pbjj6kp.mongodb.net/F3-DB?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(connection_string)

# Select the database
db = client["F3-RE"]

# Select the collections
orders_collection = db.orders
products_collection = db.products

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

# Fetch the data
orders_data = list(orders_collection.find({}, orders_fields))
products_data = list(products_collection.find({}, products_fields))

# Convert orders data to pandas DataFrame
orders_list = []
for order in orders_data:
    for item in order.get('line_items', []):
        orders_list.append({
            "customer_id": order['customer_id'],
            "product_id": str(item['product_id']),  # Convert product_id to str
            "product_name": item['name']
        })

orders_df = pd.DataFrame(orders_list)

# Convert products data to pandas DataFrame
products_list = []
for product in products_data:
    for category in product.get('categories', []):
        products_list.append({
            "product_id": str(product.get('id', None)),  # Convert product_id to str
            "category_id": category['id'],
            "category_name": category['name'],
            "product_name": product['name']
        })

products_df = pd.DataFrame(products_list)

# Print the DataFrames
print("\nOrders DataFrame:")
print(orders_df)

print("\nProducts DataFrame:")
print(products_df)

# Merge orders_df with products_df to get the category information for each ordered product
merged_df = orders_df.merge(products_df, on="product_id", how="left")

# Function to recommend products from different categories
def recommend_products(customer_id):
    # Get the categories the customer has purchased from
    customer_purchased_categories = merged_df[merged_df['customer_id'] == customer_id]['category_id'].unique()
    
    # Filter out products already purchased by the customer
    filtered_products = products_df[~products_df['category_id'].isin(customer_purchased_categories)]
    
    # Group by category and select the top products by count
    top_products = filtered_products.groupby('category_id').apply(lambda x: x.sort_values(by='product_id').head(3)).reset_index(drop=True)
    
    return top_products[['category_id', 'category_name', 'product_id', 'product_name']]

# Example: Get recommendations for a specific customer
customer_id = '26300'  # Replace with a valid customer_id
recommendations = recommend_products(customer_id)

print("\nRecommendations:")
print(recommendations)
