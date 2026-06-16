#ques 1
class BankAccount:

    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient!")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.__balance)

    def get_balance(self):
        print("Current Balance:", self.__balance)


account1 = BankAccount()

account1.deposit(2000)

account1.withdraw(5000)

account1.get_balance()

print("--------------------")

account2 = BankAccount()

account2.deposit(500)

account2.withdraw(12000)

account2.get_balance()






#ques 2
class Person:

    def walk(self):
        print("Person is walking")

    def talk(self):
        print("Person is talking")


class Teacher(Person):

    def teach(self):
        print("Teacher is teaching")


class Student(Person):

    def study(self):
        print("Student is studying")


teacher = Teacher()

teacher.walk()
teacher.talk()

teacher.teach()

print("------------------")

student = Student()

student.walk()
student.talk()

student.study()



#ques 3
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def receipt(self):
        pass


class GPay(Payment):

    def pay(self):
        print("Payment made using GPay")

    def receipt(self):
        print("GPay receipt generated")


class CreditCard(Payment):

    def pay(self):
        print("Payment made using Credit Card")

    def receipt(self):
        print("Credit Card receipt generated")


gpay = GPay()

gpay.pay()
gpay.receipt()

print("------------------")

card = CreditCard()

card.pay()
card.receipt()

'''Section 2 — Exception Handling'''

#ques 4
class InvalidAgeError(Exception):
    pass


class InvalidMarksError(Exception):
    pass


try:
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    if age < 15 or age > 30:
        raise InvalidAgeError("Age must be between 15 and 30.")

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Student registered successfully!")

except InvalidAgeError as e:
    print("InvalidAgeError:", e)

except InvalidMarksError as e:
    print("InvalidMarksError:", e)

except ValueError:
    print("Please enter valid numeric values for age and marks.")

finally:
    print("Registration done.")




#ques 5
filename = input("Enter filename: ")

try:
    file = open(filename, "r")

    lines = file.readlines()

    if len(lines) == 0:
        print("File is empty!")
    else:
        print("Total number of lines:", len(lines))

    file.close()

except FileNotFoundError:
    print("File does not exist!")

finally:
    print("complete!")




'''Section 3 — Data Structures '''

#ques 6

cities = ["Bhopal", "Indore", "Delhi", "Mumbai",
          "Pune", "Jaipur", "Hyderabad", "Chennai"]

print("First 4 cities:", cities[:4])

print("Last 4 cities:", cities[-4:])

cities.append("Kolkata")
print("After adding a city:", cities)

cities.pop(0)
print("After removing first city:", cities)

city_tuple = tuple(cities)

print("Tuple:", city_tuple)



#ques 7
students = {"rohit", "sajal", "aryan", "rohit", "Priya", "sajal", "Karan", "prince"}

print("Student Set:", students)

students.add("Vanshika")
students.add("vikas")

print("Updated Student Set:", students)

print("--------------------")

marks_dict = {
    "rohit": 82,
    "sajal": 68,
    "aryan": 55,
    "Prince": 91
}

for student, marks in marks_dict.items():

    if marks >= 75:
        print(student, "-", marks, ": Distinction")

    elif marks >= 60:
        print(student, "-", marks, ": Pass")

    else:
        print(student, "-", marks, ": Fail")





'''Section 4 — File Handling and JSON'''
#ques 8
import os

file = open("employees.txt", "w")

file.write("Anju - 30000\n")
file.write("payal - 35000\n")
file.write("talah - 40000\n")
file.write("swaleha - 45000\n")
file.write("shivani - 50000\n")

file.close()

print("Initial File Content:")
file = open("employees.txt", "r")
print(file.read())
file.close()

file = open("employees.txt", "a")

file.write("rahul - 55000\n")
file.write("Ankit - 60000\n")

file.close()

print("Updated File Content:")
file = open("employees.txt", "r")
print(file.read())
file.close()

if os.path.exists("employees.txt"):
    print("File exists.")

    os.remove("employees.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")



#ques 9
import json

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

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Data saved successfully!")

with open("students.json", "r") as file:
    data = json.load(file)

print("\nStudents with marks > 70:")

for student in data:
    if student["marks"] > 70:
        print(student["name"], "-", student["marks"])

print("\nTotal number of students:", len(data))

'''Section 5 — API and Web Scraping'''

#ques 10
import requests
import json

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:

        users = response.json()

        print("User Details:\n")

        for user in users:
            print("Name :", user["name"])
            print("Email:", user["email"])
            print("Phone:", user["phone"])
            print()

        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        print("Data saved to users.json")

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



import requests
from bs4 import BeautifulSoup
import json

response = requests.get("http://quotes.toscrape.com")

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []

    quotes = soup.find_all("div", class_="quote")

    print("Quotes by Albert Einstein:\n")

    for q in quotes:
        quote = q.find("span", class_="text").text

        author = q.find("small", class_="authors").text

        quotes_data.append({
            "quote": quote,
            "author": author
        })

        if author == "Albert Einstein":
            print(quote)
            print()

    with open("quotes.json", "w") as f:
        json.dump(quotes_data, f, indent=4)

    print("Total Quotes Scraped =", len(quotes_data))

else:
    print("Failed to fetch webpage")



   