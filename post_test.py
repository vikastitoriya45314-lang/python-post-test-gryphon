#ques 1 
# Create a class BankAccount
class BankAccount:

    # Constructor to initialize private balance variable
    def __init__(self):
        self.__balance = 10000

    # Method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.__balance)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient!")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.__balance)

    # Method to display current balance
    def get_balance(self):
        print("Current Balance:", self.__balance)


# Create first bank account object
account1 = BankAccount()

# Deposit money into account1
account1.deposit(2000)

# Withdraw money from account1
account1.withdraw(5000)

# Display balance of account1
account1.get_balance()

print("--------------------")

# Create second bank account object
account2 = BankAccount()

# Deposit money into account2
account2.deposit(500)

# Withdraw money from account2
account2.withdraw(12000)

# Display balance of account2
account2.get_balance()






#ques 2
# Parent class
class Person:

    # Method to walk
    def walk(self):
        print("Person is walking")

    # Method to talk
    def talk(self):
        print("Person is talking")


# Child class Teacher inheriting Person
class Teacher(Person):

    # Method to teach
    def teach(self):
        print("Teacher is teaching")


# Child class Student inheriting Person
class Student(Person):

    # Method to study
    def study(self):
        print("Student is studying")


# Create Teacher object
teacher = Teacher()

# Call inherited methods
teacher.walk()
teacher.talk()

# Call Teacher's own method
teacher.teach()

print("------------------")

# Create Student object
student = Student()

# Call inherited methods
student.walk()
student.talk()

# Call Student's own method
student.study()



#ques 3
# Import ABC and abstractmethod for creating abstract class
from abc import ABC, abstractmethod


# Abstract class Payment
class Payment(ABC):

    # Abstract method pay
    @abstractmethod
    def pay(self):
        pass

    # Abstract method receipt
    @abstractmethod
    def receipt(self):
        pass


# Child class GPay
class GPay(Payment):

    # Implement pay method
    def pay(self):
        print("Payment made using GPay")

    # Implement receipt method
    def receipt(self):
        print("GPay receipt generated")


# Child class CreditCard
class CreditCard(Payment):

    # Implement pay method
    def pay(self):
        print("Payment made using Credit Card")

    # Implement receipt method
    def receipt(self):
        print("Credit Card receipt generated")


# Create GPay object
gpay = GPay()

# Call methods
gpay.pay()
gpay.receipt()

print("------------------")

# Create CreditCard object
card = CreditCard()

# Call methods
card.pay()
card.receipt()

'''Section 2 — Exception Handling'''

#ques 4
# Create custom exception for invalid age
class InvalidAgeError(Exception):
    pass


# Create custom exception for invalid marks
class InvalidMarksError(Exception):
    pass


try:
    # Take input from user
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    # Check age validity
    if age < 15 or age > 30:
        raise InvalidAgeError("Age must be between 15 and 30.")

    # Check marks validity
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    # If all inputs are valid
    print("Student registered successfully!")

# Handle InvalidAgeError
except InvalidAgeError as e:
    print("InvalidAgeError:", e)

# Handle InvalidMarksError
except InvalidMarksError as e:
    print("InvalidMarksError:", e)

# Handle wrong data type input
except ValueError:
    print("Please enter valid numeric values for age and marks.")

# Finally block
finally:
    print("Registration done.")




# ques 5 
# Ask user to enter filename
filename = input("Enter filename: ")

try:
    # Open the file in read mode
    file = open(filename, "r")

    # Read all lines from file
    lines = file.readlines()

    # Check if file is empty
    if len(lines) == 0:
        print("File is empty!")
    else:
        # Print total number of lines
        print("Total number of lines:", len(lines))

    # Close the file
    file.close()

# Handle file not found error
except FileNotFoundError:
    print("File does not exist!")

# Finally block
finally:
    print("complete!")




'''Section 3 — Data Structures '''

 #ques 6    

# Create a list of 8 city names
cities = ["Bhopal", "Indore", "Delhi", "Mumbai",
          "Pune", "Jaipur", "Hyderabad", "Chennai"]

# Print first 4 cities
print("First 4 cities:", cities[:4])

# Print last 4 cities
print("Last 4 cities:", cities[-4:])

# Add a new city at the end
cities.append("Kolkata")
print("After adding a city:", cities)

# Remove the first city
cities.pop(0)
print("After removing first city:", cities)

# Convert list to tuple
city_tuple = tuple(cities)

# Print tuple
print("Tuple:", city_tuple)



#ques 7
# Create a set of students (with duplicates)
students = {"rohit", "sajal", "aryan", "rohit", "Priya", "sajal", "Karan", "prince"}

# Print set (duplicates are automatically removed)
print("Student Set:", students)

# Add 2 new students
students.add("Vanshika")
students.add("vikas")

# Print updated set
print("Updated Student Set:", students)

print("--------------------")

# Create a dictionary of students and their marks
marks_dict = {
    "rohit": 82,
    "sajal": 68,
    "aryan": 55,
    "Prince": 91
}

# Loop through dictionary
for student, marks in marks_dict.items():

    if marks >= 75:
        print(student, "-", marks, ": Distinction")

    elif marks >= 60:
        print(student, "-", marks, ": Pass")

    else:
        print(student, "-", marks, ": Fail")





'''Section 4 — File Handling and JSON'''
#ques 8
# Import os module
import os

# Create employees.txt and write 5 employees with salary
file = open("employees.txt", "w")

file.write("Anju - 30000\n")
file.write("payal - 35000\n")
file.write("talah - 40000\n")
file.write("swaleha - 45000\n")
file.write("shivani - 50000\n")

file.close()

# Read and print the file
print("Initial File Content:")
file = open("employees.txt", "r")
print(file.read())
file.close()

# Append 2 more employees
file = open("employees.txt", "a")

file.write("rahul - 55000\n")
file.write("Ankit - 60000\n")

file.close()

# Read and print updated file
print("Updated File Content:")
file = open("employees.txt", "r")
print(file.read())
file.close()

# Check if file exists
if os.path.exists("employees.txt"):
    print("File exists.")

    # Delete the file
    os.remove("employees.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")



#ques 9
# Import json module
import json

# Create a list of 4 students
students = [
    {
        "name": "Amit",
        "age": 20,
        "city": "Bhopal",
        "course": "B.Tech",
        "marks": 82
    },
    {
        "name": "prayag",
        "age": 21,
        "city": "Indore",
        "course": "BCA",
        "marks": 68
    },
    {
        "name": "kumkum",
        "age": 22,
        "city": "Delhi",
        "course": "B.Tech",
        "marks": 91
    },
    {
        "name": "Pranjal",
        "age": 20,
        "city": "Mumbai",
        "course": "B.Sc",
        "marks": 75
    }
]

# Save data to students.json with indent=4
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Data saved successfully!")

# Read data from students.json
with open("students.json", "r") as file:
    data = json.load(file)

# Print students with marks greater than 70
print("\nStudents with marks > 70:")

for student in data:
    if student["marks"] > 70:
        print(student["name"], "-", student["marks"])

# Print total number of students
print("\nTotal number of students:", len(data))

'''Section 5 — API and Web Scraping'''

#ques 10
import requests
import json

try:
    # API call
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    # Check status code
    if response.status_code == 200:

        users = response.json()

        print("User Details:\n")

        # Print Name, Email, Phone
        for user in users:
            print("Name :", user["name"])
            print("Email:", user["email"])
            print("Phone:", user["phone"])
            print()

        # Save data to JSON file
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        print("Data saved to users.json")

        # Total users
        print("Total Users =", len(users))

    else:
        print("Failed to fetch data")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("API Error:", e)

except Exception as e:
    print("Error:", e)

finally:
    print("Program over")



#ques 11
import requests
from bs4 import BeautifulSoup
import json

# Get webpage data
response = requests.get("http://quotes.toscrape.com")

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []

    # Find all quote blocks
    quotes = soup.find_all("div", class_="quote")

    print("Quotes by Albert Einstein:\n")

    for q in quotes:
        quote = q.find("span", class_="text").text

        # Intentional Error Here
        author = q.find("small", class_="authors").text

        # Store data
        quotes_data.append({
            "quote": quote,
            "author": author
        })

        # Print only Einstein quotes
        if author == "Albert Einstein":
            print(quote)
            print()

    # Save all quotes to JSON file
    with open("quotes.json", "w") as f:
        json.dump(quotes_data, f, indent=4)

    print("Total Quotes Scraped =", len(quotes_data))

else:
    print("Failed to fetch webpage")



   