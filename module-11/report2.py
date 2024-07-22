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

# Function to display Supplier Supply Summary Report
def display_supplier_supply_summary():
    cursor.execute("""
        SELECT s.SupplierName, sp.SupplyType, sp.Quantity
        FROM Supplier s
        JOIN Supply sp ON s.SupplierID = sp.SupplierID
    """)
    rows = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print("\nSupplier Supply Summary Report")
    print(tabulate(rows, headers, tablefmt='psql'))

# Display Supplier Supply Summary Report
display_supplier_supply_summary()

# Close the connection
cursor.close()
connection.close()
