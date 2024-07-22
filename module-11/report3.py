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

# Function to display Order Details Report
def display_order_details():
    cursor.execute("""
        SELECT o.OrderID, o.OrderDate, d.DistributorName, w.WineName, od.Quantity
        FROM Orders o
        JOIN Distributor d ON o.DistributorID = d.DistributorID
        JOIN OrderDetails od ON o.OrderID = od.OrderID
        JOIN Wine w ON od.WineID = w.WineID
    """)
    rows = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print("\nOrder Details Report")
    print(tabulate(rows, headers, tablefmt='psql'))

# Display Order Details Report
display_order_details()

# Close the connection
cursor.close()
connection.close()
