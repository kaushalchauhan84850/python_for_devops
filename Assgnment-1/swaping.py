# Swap two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swap: a = {a}, b = {b}")

c = a
a = b
b = c

print(f"After swap (method 1): a = {a}, b = {b}")


a = a + b
b = a - b
a = a - b
print(f"After swap (method 2): a = {a}, b = {b}")


name = "karan"
surnme ="chauhan"
print(f"Before swap: name = {name}, surname = {surnme}")
name, surnme = surnme, name
print(f"After swap: name = {name}, surname = {surnme}")
