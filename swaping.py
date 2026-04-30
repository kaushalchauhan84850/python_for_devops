# Swap two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swap: a = {a}, b = {b}")

c = a
a = b
b = c

print(f"After swap (method 1): a = {a}, b = {b}")
