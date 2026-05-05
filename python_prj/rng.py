from random import randint


min_number = int(input('Enter the minimum number: '))
max_number = int(input("Enter the maximum number: "))

if (max_number < min_number):
    print("Error: Maximum number must be greater than or equal to minimum number.")
else:
    random_number = randint(min_number, max_number)
    print(random_number)
  
