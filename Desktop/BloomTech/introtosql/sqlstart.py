
'''This is my first file for practicing SQL.'''

# SQL CONSTRUCTS

# typical SQL query
SELECT name, id, address, customer_since
FROM customers
WHERE state = "CA";

import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM armory_item;'
curs.execute(query)
curs.execute(query).fetchall()


#challenge query

#Imagine the customers table also has
#address and customer_since attributes
#(where customer_since is a year). Write
#a query to get all names and addresses of
#customers living in Colorado who have been
#customers for at least 10 years.

SELECT name, address
FROM customers
WHERE state = "Colorado"
GROUP customer_since = customer_since > "2012"

import sqlite3
conn = sqlite3.connect("rpg_db.sqlite3")
curs = conn.cursor()
query = "SELECT COUNT(*) FROM armory_item;"
curs.exectute(query)
curs.execute(query).fetchall()

