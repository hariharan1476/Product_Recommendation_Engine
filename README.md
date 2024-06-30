# Product_Recommendation_Engine

CRE - Category based Recommendation Engine


LOAP - List Of All Prodcuts


OPC_in_DF - Orders,Products,Customers fetching datas in DataFrame


RE - Recommendation Engine (Recommend a Product From Top 3 Most Selling Products with Removing a customers already Purchased Products and unwanted Products)


SPL - Specified Product List removing Top 3 Recommendation


TOP3 - Recommending a Top 3 Most selling products


#Prelims


	1.	Install Python:
Ensure you have Python installed. You can download and install it from python.org. After installation, verify it by running:



python3 --version


	2.	Install VS Code:
If you haven’t already, download and install Visual Studio Code from code.visualstudio.com.
	3.	Install Python Extension for VS Code:
Open VS Code and install the Python extension:
	1.	Go to the Extensions view by clicking on the square icon in the sidebar or pressing Ctrl+Shift+X.
	2.	Search for “Python” and install the extension provided by Microsoft.
	4.	Create a Virtual Environment:
Open the terminal in VS Code by clicking on the terminal icon or using the shortcut Ctrl+ or Cmd+ (for macOS).
Navigate to your project directory:



cd /path/to/your/project



Create a virtual environment using venv:



python3 -m venv venv



	5.	Activate the Virtual Environment:
Activate the virtual environment you created:



source venv/bin/activate



You should see (venv) at the beginning of your terminal prompt, indicating that the virtual environment is active.

	6.	Select the Interpreter in VS Code:
	1.	Open the Command Palette by pressing Cmd+Shift+P.
	2.	Type Python: Select Interpreter and press Enter.
	3.	Select the interpreter from your virtual environment. It will look something like .venv/bin/python.
	7.	Verify the Setup:
To ensure everything is set up correctly, create a simple Python script and run it:



print("Hello, Virtual Environment!")



Run the script using the VS Code terminal to check if it works as expected.

	8.	Install Packages:
You can now install any packages you need within this virtual environment using pip:




pip install <package-name>


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
