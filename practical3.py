# Practicing python loops and Logical Conditionds 
# 1. Python Operators 
import random
a = 10
b = random.randint(0,20)
c = 100
print("a is", a, "and", "b is", b)
print("The answer to a + b is", a + b)
print("a < b is", a < b)
print("a == b is", a == b)
print("a + b is", a + b)
print("a * b is", a * b)
print("a to the power of b is", a ** b)
 
# 2. If-Else Statement 
a = 33
b = 200
if b > a:
    print("b is greater than a")
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Match Case statement 
def main():
    day = 8
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Not a weekday")
main()

# While Loop
import random
b=random.randint(0,10)
c=100
while c!=b:
    c=int(input("Enter your Guess"))
    if c==b:
        print("Tashi Delek,You Won !")
        break
    else:
        print("AHh, You lose! Try Again")
 # Write a Python program that uses a while loop to print the numbers from 1 to 10       
i=1
while i<=10:
    print(i)
    i=i+1

    