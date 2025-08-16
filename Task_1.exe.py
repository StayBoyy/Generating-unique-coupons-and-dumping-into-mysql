"""
TASK-1

Generate 1 Lakh coupons(unique) and dump it into my sql
Reduce the time complexity of code execution

"""

import pymysql as mahi
import random
import string

# This Function is used  to generate a unique alphanumeric coupon code
def generate_coupon_code(length=8):  # Generated for 8 because my name has 8 letters in it -->> Mahender
    characters = string.ascii_uppercase + string.digits  # This  Contains A-Z and 0-9
    return ''.join(random.choice(characters) for _ in range(length))


# Establish connection to the database
db = mahi.connect(
    host="localhost",  # Database host-->> usually 'localhost'
    port=3306,  # The port for MySQL, default is -->> 3306
    user="root",  # MySQL-->> username
    password="root",  # MySQL-->> password
    db="zomato_coupons"  # The database where my table is located in MYSQL
)

print("Connected to the database:", db)  # Making sure that the connection has established or not

# Created a cursor object to interact with the database(MYSQL Database)
cursor = db.cursor()

cursor.execute("SELECT * FROM food;")  # It Selects data from the food table to check the connection
for row in cursor.fetchall():
    print(row)  # It Prints each row from the food table

# Here I have generated and inserted 100,000 unique coupons
coupons = set()  # I have used a "set" to ensure that all coupon codes are unique and maps accordingly

while len(coupons) < 100000:  # This will  Keep generating unique coupons until 100,000
    coupons.add(generate_coupon_code())  # Here after generating we "Add" a new coupon code to the set

coupons = list(coupons)  # converting set into list for easier batch process

batch_size = 1000  # Defining the size of the batch for inserting rows(1000 at a time)

for i in range(0, len(coupons), batch_size):
    batch = coupons[i:i + batch_size]  # It extracts a portion of the list from index i to i + batch_size - 1.
    values = ', '.join([f"('user', '{code}', 'place')" for code in batch])  # It is a list comprehension that creates
    # A list of strings Each string represents a single row's values in the format ('user', 'coupon_code', 'place').

    insert_query = f"INSERT INTO food (user_name, coupon_id, place) VALUES {values};" # It inserts multiple rows (1000
    # in each batch) into the food table in one operation.
    cursor.execute(insert_query)
for i in coupons:
    cursor.execute(f"INSERT INTO food (user_name, coupon_id, place) VALUES ('user', '{i}', 'place');")

db.commit()  # Commit the transaction to save changes to the database

# I want to Verify by selecting a few entries from the food table
cursor.execute("SELECT * FROM food LIMIT 10;")
for row in cursor.fetchall():
    print(row)  # Print the first 10 rows to verify the insert

# Closing the cursor and the connection
cursor.close()
db.close()

