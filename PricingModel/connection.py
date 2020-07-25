import sqlite3

conn = sqlite3.connect('PricingEngine')
print("Opened database successfully");

# cursor = conn.execute("SELECT id, name, address, email from STUDENT")

conn.execute('''CREATE TABLE STUDENT
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         EMAIL         TEXT);''')
print("Table STUDENT created successfully")