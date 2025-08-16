
"""
Task 3:
User Authentication, Registration  and Validation via CSV file data.
	— Whenever there’s a new user, update the same CSV file with new details.
"""

# importig the CVS file
import csv
import time

# Creating a CSV file named students.csv with initial entries
with open("students.csv", "w", newline='') as x:
    x = csv.writer(x)
    x.writerow(("Name", "City", "email_id", "contact"))
    x.writerow(("Mahi", "Pune", "mahendar123@gmail.com", "9834761299"))
    x.writerow(("Akash", "Mumbai", "ak4433@gmail.com", "9834331208"))
    x.writerow(("Madhav", "Delhi", "maddy987@gmail.com", "9049447202"))
    x.writerow(("Naresh", "Hyderabad", "nari1430@gmail.com", "6339003289"))

# Function to check if an email already exists in the CSV file
def check_email_exists(email):
    with open("students.csv", "r") as m:
        x = csv.reader(m)
        next(x)  # Skip the header row
        for row in x:
            if row[2] == email:  # Email is in the third column (index 2)
                return True
    return False

# Function to add a new student entry
def add_student(name, city, email, contact):
    with open("students.csv", "a", newline='') as x:  # 'a' -->> append if exist else create new one
        writer = csv.writer(x)
        writer.writerow([name, city, email, contact])

# Ask user for email
email = input("Enter the student's email: ")
print("Checking for the user, please wait for a few moments...")
# Add a delay of 3 seconds before checking if the email exists
time.sleep(3)

# Check if the email already exists
if check_email_exists(email):
    print("USER ALREADY EXISTS")
else:
    # If the email does not exist, ask for further details and add a new entry
    print("USER DOES NOT EXIST")
    print("If you want to become a user... Type the following details below")
    name = input("Enter the student's name: ")
    city = input("Enter the student's city: ")
    contact = input("Enter the student's contact: ")
    add_student(name, city, email, contact)  # Adding the details in the CSV file
    print("New student added successfully.")

# Reading from the CSV file to show updated content
with open("students.csv", "r") as m:
    x = csv.reader(m)
    for i in x:
        print(i)


