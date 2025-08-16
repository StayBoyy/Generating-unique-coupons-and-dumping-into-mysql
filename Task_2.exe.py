""""
Task 2 : User Authentication, Registration  and Validation via MySQL DB data.
"""
import pymysql as hey
import time
import sys  # Import sys to use sys.exit() for quitting the program

# Establish a connection to the MySQL database
db = hey.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='root',
    db='employee'
)
cur = db.cursor()

def verify_user(email):
    print('User is being verifing...')
    query = "SELECT email FROM empl WHERE email = %s;"
    cur.execute(query, (email,))
    result = cur.fetchone()
    return result is not None

def auth_user(email, username, password):
    print("User is being authenticated...")
    time.sleep(3)
    query = "SELECT * FROM empl WHERE email = %s AND username = %s AND password = %s;"
    cur.execute(query, (email, username, password))
    result = cur.fetchone()
    return result is not None

def user_login(email):
    verified = verify_user(email)

    if verified:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authenticated = auth_user(email, username, password)
        if not authenticated:
            print("User does not exist.\nIf you wish to become a user, type Yes and press ENTER:")
            user_interest = input("Yes/No: ").lower()

            if user_interest == 'yes':
              usname = input("Enter your username: ")
              email_id = input("Enter your email_id: ")
              paswrd = input("Enter your password: ")
              cntc = input("Enter your contact: ")
              rec = input("Enter your recovery: ")
              query = "INSERT INTO empl (username, email, password, contact,recovery) VALUES (%s, %s, %s, %s, %s);"
              cur.execute(query, (usname, email_id, paswrd, cntc,rec))
              print("User details are being captured to our DB, please wait...")
              time.sleep(4)
              print("You have been registered as a user. You can check via the login option.")
              db.commit()  # saves it to the DB
            elif user_interest == 'no':
              print("Thanks for visiting....")
            else:
             sys.exit()
        else:
             print(f"Welcome {username}")


# Example usage
(user_login("mahi@123gmail.com"))

# Close the cursor and connection after all operations are done
cur.close()
db.close()






""""

Task 2 : User Authentication, Registration and Validation via MySQL DATABASE Data.

"""
import pymysql as refer
import time

# Database Connection
db = refer.connect(
    host = "127.0.0.1",
    port = 3306,
    user = 'root',
    password = 'root',
    db = 'colleague'
)

print(db)

# Cursor initialization
cur = db.cursor()

#Verfication of email of the colleague
def verify_user(email):
    query = """Select from information where email = '{}';""".format(email)
    cur.execute(query)
    email_check = []
    for i in cur:
        email_check.append(i)
    if len(email_check)>=1:
            return True
    else:
            return False

#Authentication of the colleagues
def authen_user(username, password):
    query = """Select from information where email = '{}' AND username = '{}' AND password = '{}';""".format(email, username, password)
    cur.execute(query)
    user_check = []
    for i in cur:
        user_check.append(i)
    if len(user_check)>=1:
        return True
    else:
        return False

# User Login Information
def user_login(email, username, password):
    verification = verify_user(email)

    if verification is True:
        authenticated = authen_user(email, username, password)
        if authenticated is True:
            print(f"Welcome{username}@Company")
        else:
            print("User Authentication failed.\nPlease try again")
            cur.close()

    else:
        print("User does not exists.\nPlease type 'Yes' & press Enter: ")

    if input("Yes/No: ").lower() == 'yes':
        email_id = input("Enter user's email_id: ")
        uname = input("Enter user's username: ")
        psword = input("Enter user's password: ")
        conta = input("Enter user's contact: ")

        cur.execute(
            f"insert into information(username, email, password, contact) values('{uname}', '{email_id}', '{psword}', '{conta}');"
            )
        print("User details are being recorded of our DB, please wait...")

        db.commit()
        cur.close()
    else:
        print("Thank you for time")



# Example usage (optional)
(user_login("akash76@gmail.com", 'Akash', 'pasword123'))