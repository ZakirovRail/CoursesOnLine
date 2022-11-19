# name = 'Bob'
# greeting = f"Hello, {name}"
# print(greeting)  #  Hello, Bob
# -------------------------------------------------------------------------------------------------
# name = 'Rob'
# greeting = "Hello, {}"
# with_name = greeting.format(name)
# print(with_name)  #  Hello, Rob
# with_name_2 = greeting.format("Rolf")
# print(with_name_2)  #  Hello, Rolf

# -------------------------------------------------------------------------------------------------
# longer_phrases = "Hello {}. Today is {}"
# formated = longer_phrases.format("Ralf", "Monday")  #  Hello Ralf. Today is Monday
# print(formated)


# -------------------------------------------------------------------------------------------------
# size_input = input("How big is your house (in square feet): ")
# square_feet = int(size_input)
# square_meters = square_feet / 10.8
# print(f"{square_feet} square feet is {square_meters:.3f} square meters")

# -------------------------------------------------------------------------------------------------

# numbers = [1, 3, 5]
# doubled = [i*2 for i in [1,3,5]]
# print(doubled)

# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# start_s = [i for i in friends if i.startswith('S')]
# print(start_s)
#
#
# start_s = []
# for i in friends:
#     if i.startswith('S'):
#         start_s.append(i)
# print(start_s)


# -------------------------------------------------------------------------------------------------
# student_attendance= {"Rolf":96, "Bob":80, "Anne":100}
# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")
#
# print("===============================================")
#
# student_attendance= {"Rolf":96, "Bob":80, "Anne":100}
# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")

# -------------------------------------------------------------------------------------------------

# t = 5, 11
# x, y = t
# print(x, y)  #  5 11


# -------------------------------------------------------------------------------------------------
# people = [("Bob", 42, "Mechanic"), ("Anna", 21, "engineer"), ("Paul", 61, "Manager")]
#
# for name, age, profession in people:
#     print(f"Name:{name}, Age:{age}, Profession:{profession}")


# -------------------------------------------------------------------------------------------------
# head, *tail = [1,2,3,4,5]
# print(head)
# print(tail)
#
# *head, tail = [1,2,3,4,5]
# print(head)
# print(tail)


# -------------------------------------------------------------------------------------------------

# add = lambda x, y: x + y
# print(add(5, 7))
#
# add = (lambda x, y: x + y)(10, 10)
# print(add)
# -------------------------------------------------------------------------------------------------
# def double(x):
#     return x * 2
#
# sequence = [1,3,5,7]
# doubled = [double(x) for x in sequence]
# print(doubled)
# #OR
# doubled2 = map(double, sequence)
# print(list(doubled2))
#
# doubled3 = [(lambda x: x * 2)(x) for x in sequence]
# print(doubled3)
#
# doubled4 = map(lambda x: x * 2, sequence)
# print(list(doubled4))
# print(doubled4)

# -------------------------------------------------------------------------------------------------
# dictionary comprehensions


# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234")
# ]

# username_mapping= {user[1]: user for user in users}
# print(username_mapping)
# print(username_mapping["Bob"])


# Example
# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234")
# ]
#
#
# username_mapping = {user[1]: user for user in users}
# username_input = input("Enter your name: ")
# password_input = input("Enter your password: ")
# _, username, password = username_mapping[username_input]
#
# if password_input == password:
#     print("Your details are correct")
# else:
#     print("Your details are incorrect")

# -------------------------------------------------------------------------------------------------

# grades= {1,3,5,7,9}
# sum = 0
# for i in grades:
#     sum += int(i)
# print(sum)
#
# sum2 = lambda sum = 0: for i in grades sum +=i


# -------------------------------------------------------------------------------------------------
# def add(x, y):
#     return x + y
#
# nums = [1, 3]
# print(add(*nums))  #  4
#
#
# def add(x, y):
#     return x + y
#
# nums = {'x':15, 'y':20}
# print(add(**nums))  #  35


# -------------------------------------------------------------------------------------------------
# def named(**kwargs):
#     print(kwargs)
# named(name='Bob', age=25)  #  {'name': 'Bob', 'age': 25}


# def named(name, age):
#     print(name, age)
# details= {"name":'Bob', "age":25}
# named(**details)  #  Bob 25


# def named(**kwargs):
#     print(kwargs)
#
# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")
#
# print_nicely(name="Bob", age=25)


# -------------------------------------------------------------------------------------------------
# student = {"name":"Rolf", "grades":(89,90,93,78,90)}
# def average(sequence):
#     return sum(sequence) / len(sequence)
# print(average(student["grades"]))  #  88.0

# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (89,90,93,78,90)
#
# example= Student()
#
# print(example.name)  #  Rolf
# print(example.grades)  # (89, 90, 93, 78, 90)


# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (89,90,93,78,90)
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student = Student()
# print(Student.average(student))  #  88.0
# print(student.average())  #  88.0


# -------------------------------------------------------------------------------------------------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# bob = Person('Bob', 53)
#
# print(bob)  #  <__main__.Person object at 0x0000000000432518>
# print(bob.name)  #  Bob
# print(bob.age)  #  53


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Person: {self.name}, {self.age} yeas old"
#
# bob = Person('Bob', 53)
#
# print(bob)  #  Person: Bob, 53 yeas old
# print(bob.name)  #  Bob
# print(bob.age)  #  53


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Person: {self.name}, {self.age} yeas old"
#
#     def __repr__(self):
#         return f"(<Person: {self.name}, {self.age}>)"

# bob = Person('Bob', 53)
#
# print(bob)  #  Person: Bob, 53 yeas old
# print(bob.__repr__())  #  (<Person: Bob, 53>)
# print(bob.name)  #  Bob
# print(bob.age)  #  53
# -------------------------------------------------------------------------------------------------


# class Store:
#
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add(self, name, price):
#         item = {"name": name, "price": price}
#         self.items.append(item)
#
#     def stock_price(self):
#         total = 0
#         for item in self.items:
#             total += item['price']
#         return total
## return sum([item['price'] for item in self.items])

# -------------------------------------------------------------------------------------------------

# class Store:
#
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add(self, name, price):
#         self.items.append({
#             "name": name,
#             "price": price})
#
#     def stock_price(self):
#         total = 0
#         for item in self.items:
#             total += item['price']
#         return total
#         # return sum([item['price'] for item in self.items])
#
#     @classmethod
#     def franchise(cls, store):
#         new_store = Store(store.name + " - franchise")
#         return new_store
#
#     @staticmethod
#     def store_details(store):
#         return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

# -------------------------------------------------------------------------------------------------
# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True
#
#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"
#
#     def disconnect(self):
#         self.connected = False
#         print("Disconnected.")
#
#
# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_pages = capacity
#
#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
#
#     def print(self, pages):
#         if not self.connected:
#             print("Your printer is not connected!")
#             return
#         print(f"Printing {pages} pages.")
#         self.remaining_pages -= pages
#
# printer = Printer("Printer", "USB", 500)
# printer.print(20)
# print(printer)


# -------------------------------------------------------------------------------------------------

# class BookShelf:
#     def __init__(self, *books):
#         self.books = books
#
#     def __str__(self):
#         return f"BookShelf with {len(self.books)} books."
#
#
# class Book:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"Book {self.name}"
#
# book = Book("Harry Poter")
# book2 = Book("Python 101")
#
# shelf = BookShelf(book, book2)
# print(shelf)

# -------------------------------------------------------------------------------------------------
# from typing import List
#
#
# def list_avg(sequence: List) -> float:
#     return sum(sequence) / len(sequence)
#
#
# list_avg(123)

# -------------------------------------------------------------------------------------------------
# def search(sequence, expected, finder):
#     for elem in sequence:
#         if finder(elem) == expected:
#             return elem
#     raise RuntimeError(f"Could not find an element with {expected}")
#
#
# friends = [
#     {"name":"Rolf Smith", "age":24},
#     {"name":"Adam Wool", "age":30},
#     {"name":"Anne Pun", "age":27}
# ]
#
# def get_friend_name(friend):
#     return friend["name"]
#
# print(search(friends, "Rolf Smith", get_friend_name))



# -------------------------------------------------------------------------------------------------
# user = {"username":"Jose", "access_level":"guest"}
#
#
# def get_admin_password():
#     return "1234"
#
#
# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."
#     return secure_function
#
# get_admin_password = make_secure(get_admin_password())
# print(get_admin_password())


#OR
# user = {"username":"Jose", "access_level":"guest"}
#
#
# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."
#     return secure_function
#
#
# @make_secure
# def get_admin_password():
#     return "1234"
#
#
# print(get_admin_password())  #  No admin permissions for Jose.
# print(get_admin_password.__name__)  # secure_function


# to solve problem with changing name of origin function we should use the functools library
# import functools
# user = {"username":"Jose", "access_level":"guest"}
#
#
# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."
#     return secure_function
#
#
# @make_secure
# def get_admin_password():
#     return "1234"
#
#
# print(get_admin_password())  #  No admin permissions for Jose.
# print(get_admin_password.__name__)  # get_admin_password








# -------------------------------------------------------------------------------------------------
# Improving decorators - decorators with parameters
import functools



def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"
        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("guest")
def get_dashboard_password():
    return "user:user_password"


user = {"username":"Jose", "access_level":"guest"}
print(get_admin_password())  #  No admin permissions for Jose
print(get_dashboard_password())  #  user:user_password
print("===================================================")
user = {"username": "Anna", "access_level": "admin"}
print(get_admin_password())  #  admin: 1234
print(get_dashboard_password())  #  No guest permissions for Anna




# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
