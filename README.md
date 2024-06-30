# Product_Recommendation_Engine

CRE - Category based Recommendation Engine


LOAP - List Of All Prodcuts


OPC_in_DF - Orders,Products,Customers fetching datas in DataFrame


RE - Recommendation Engine (Recommend a Product From Top 3 Most Selling Products with Removing a customers already Purchased Products and unwanted Products)


SPL - Specified Product List removing Top 3 Recommendation


TOP3 - Recommending a Top 3 Most selling products


#Requirements


1.MongoDb Coonection String


2.DataBase Name


3.Orders,Prodcuts,Customers Tables


{  
  orders table required column name is

  customer_id
  line_items.product_id
  line_items.name

  products table required column name is

  categories.id
  categories.name
  name

  customers table required column name is 
  id
}


#Libraries


pip install pymongo


pip install pandas


#MY_MONGODB_CREDNTIALS


Connection String = "mongodb+srv://techvaseegrah:kL5RvAyrOQBVFQAc@cluster0.pbjj6kp.mongodb.net/F3-DB?retryWrites=true&w=majority&appName=Cluster0"


DB_Name = "F3-RE"
