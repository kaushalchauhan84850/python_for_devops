str1 = "this is my first python code"
find = input("Enter the number or word you want to find:")
print(find in str1)


# this is use to find anything in the string it can be number and string but the input shiuld be string to get itrated 
# if the value is present in the string it will return true and if not it will return false

# it is also uses to validate things 
# for example

email = input("Enter your email:")
find = "@gmail.com"
print(find in email)

# there are two type of membership opertaor in python one is in and another is not in
# in is used to find the value in the string and not in is used to find the value is not present in the string

poem = """twinkle twinkle little star
how i wonder what you are
up above the world so high
like a diamond in the sky"""
find = input("Enter the word you want to find in the poem:")
print(find not in poem)


#we can also use it in conditionals statements

email = input("Enter your email:")
find = "@gmail.com"
if find in email:
    print("This is a valid email")
else:
    print("This is not a valid email")
    
    
    
# have have learned about if else statement 
# let do a expample of this 
age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
    
    
# we can also use elif statement in python to check multiple conditions

age = int(input("Enter your age:"))
if age < 18:
    print("You are a child")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")
    
    
    
                
