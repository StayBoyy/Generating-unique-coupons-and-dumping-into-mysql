"""
Task 5 :
"""
## 1: Python program to get sum of the two numbers

m = float(input("first number:"))
n = float(input("second number:"))
x = m + n
print("sum of the two numbers is", x)


###############################################################################################


## 2: Python program to find the greatest of three numbers.

# Input: Three numbers
num1 = float(input("Entering the first number: "))
num2 = float(input("Entering the second number: "))
num3 = float(input("Entering the third number: "))

# Finding the greatest number
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

# Output: The greatest number
print(f"The greatest of the three numbers is: {greatest}")


##########################################################################################################


## 3: Python program to find the smallest number in a list.
# Let us take some random list

k = [43, 7, 21, -61, 1, 248, -840, 91, 3000]

# Initialize a variable to store the smallest number Start with the first element in the list
smallest = k[0]

# Iterate through each number in the list
for i in k:
    # If the current number is smaller than the smallest, update the smallest
    if i < smallest:
        smallest = i

# Output the smallest number
print(f"The smallest number in the list is: {smallest}")

#############################################################################################


## 4: Python program to find the greatest number in a list.
# Let us take some random list

k = [43, 7, 21, -61, 1, 248, -840, 91, 3000]

# Initialize a variable to store the greatest number Start with the first element in the list
greatest = k[0]

# Iterate through each number in the list
for i in k:
    # If the current number is greater than the greatest, update the greatest
    if i > greatest:
        greatest = i

# Output the greatest number
print(f"The greatest number in the list is: {greatest}")

##########################################################################################


## 5 :Python program to print duplicates from a list of integers.
# Sample list of integers
numbers = [4, 4, 6, 7, 6]
dummy = []
for i in range(len(numbers)):
   for j in range(i+1,len(numbers)):
       if numbers[i] == numbers[j]:
           dummy.append(numbers[i])

print("Duplicates are :",dummy)


##############################################################################################

## 6: Python program to check if a given number is prime or not.

number = int(input("Enter the number: "))

def isprime (number):
    if number <= 1:
        # print("none")

        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

if isprime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

################################################################################################


## 7: Python code to check if a given character is digit or not

x = input("Enter any random character: ")

# Check if the input is a digit
if '0' <= x <= '9':
    print("It is a digit")
else:
    print("Not a digit")
    
#### OR
x = input("Enter any random character: ")

# Check if the input is a digit
if x.isdigit():
    print("It is a digit")
else:
    print("Not a digit")

#########################################################################################


# 8 :Python code to check if a given character is a vowel or consonant.
x = input("Enter a random alphabet :").lower()

vowels = ["a","e","i","o","u"]

if x in vowels:
    print("vowel")

else:
    print("consonant")
    





