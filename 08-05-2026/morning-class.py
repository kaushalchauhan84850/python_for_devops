

# loops in python 
# for loop : ranged based 
# while loop : condition based


# 1. for loop 
# for i in range(start, end, step):

num = int(input("enter the number:"))
name = "aman"
for i in range(num):
    print(f"{name}", end=" ")


# we can also break the loop using break statement
# at any range we want to break

for i in range(1,15):
    if i == 10:
        break
    print(i, end=" ")

# and we can also skip the iteration using continue statement

for i in range(1,15):
    if i == 10:
        continue
    print(i, end=" ")

# to print the even numbers from 1 to 20

for i in range(1,20):
    if i%2 == 0:
        print(i, end=" ")


# we can also use it to sum sequance of number 

sum = 0
for i in range(1,11):
    sum += i
print(f"\nthe sum of first 10 natural number is: {sum}")


# if we wart to multiply we have to start it from 1 and have to 


# and we can also run the loop in reverse order
for i in range(10,0,-1):
    print(i, end=" ")