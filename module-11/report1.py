import mysql.connector
from tabulate import tabulate

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Peppabeppa12.',
    database='BacchusWinery'
)

cursor = connection.cursor()

# Function to display Wine Inventory Report
def display_wine_inventory():
    cursor.execute("SELECT WineName, Type, Price FROM Wine")
    rows = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print("\nWine Inventory and Price Report")
    print(tabulate(rows, headers, tablefmt='psql'))

# Display Wine Inventory Report
display_wine_inventory()

# Close the connection
cursor.close()
connection.close()
