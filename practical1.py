# 1. Creating a function 
def my_function():
  print("Hello from a function")
    # Calling the function
my_function() 
# 2. Scope 
def func():
    # Local scope
    s = "Me too! (on local scope)"
    print(s)
    # Global scope
s = "I love python! (on global scope)"
print(s)
# 3. Basic data types 
  # Integer
pi = 3.14
pi2 = int(pi)
print(pi)
print(pi2)

  # Float
pi3 = "3.14"
print(type(pi3))
pi4 = float(pi3)
print(type(pi4))

  # Boolean
print(0<1)
print(1>0)
bool(0)
bool(1)
bool("Hello")

  # None
x = None
print(x)
 
 # String and Manipulation
print("Hello!!!!")
print("This is my first script!")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String functions
print(len(a))
print(a.upper())
print(a.lower())
print(a.count('i'))
print(a.find('d'))
print(a.split())

# String Concatenation
b = "Hello"
c = "Hello"
d = b + "!!" + c + "??"
print(d)

# String replication
print("Alice" * 5)

# String formatting
name = "Karma"
print(f"Hello {name}")
print("Greeting to you, {}".format(name))
Number = 2
print("There are %d %s in the class" %(Number, name))

# Basic Data Structure 
# List
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist.index("banana"))
thislist.remove("banana")
thislist.insert(1, "strawberry")
print(thislist)

# Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(len(thisset))
print(type(thisset))

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

#  Class Exercise 
# Q1. Array manipulation:
      # Refer to the following documentation on python list methods Link
      # Create a python list and name it first_list as shown below:
first_list=[1,2,3,4,5,6,7,8]
      # Create a second empty list named inverse_list:
inverse_list=[]
      # Using the .append() .pop() methods, create the implementation of a stack whereby you de-que elements from the first list and enqueee them into the second list. Your output must be as follows:
      #inverse_list = [9,8,7,6,5,4,3,2,1,0]
index=7
while index >= 0:
    item = first_list.pop(index)
    inverse_list.append(item)
    index -= 1
print(inverse_list)
# 2. Implementing Function
     # Take your array invers implementation from question 1 and define a function known as reverse_array. 
     # Pass the first_list() as an argument into the array and ensure that inverse_list is returned when the function is called.
def reverse_array(first_list):
      reverse_array(first_list)




      

    