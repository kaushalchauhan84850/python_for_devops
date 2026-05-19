# what are funtion in python 
# every function have there own pourpose
#2. function is a block of code (code) which exicute insdie its own block 
#3. function is re-usable means define one time use many times (DRY)
#4. function have two main part forst function defination and second function calling.
# in python bydefault function return "none"

# how to define function in python 

# def add(): # parameter
#     a = 20
#     b = 10
#     c = a+b
#     print(c)
    
# add() #arguments 


# function divides into fout catagory 
#1. take nothing return nothing
#2. taek nothing return something 
#3. take something return something
#4. take something return nothing


# parameters(para) and arguments (args) .
# positiion parameter and argument 
#default

# def add(a,b): # positining parameter
#     c = a+b
#     print(c)
# add(10,20) # positining arguments 

# add(4,5)

# waf to print table

# def table_print(n):
#     for i in range(1,11):
#         print(f"{i}x{n}={i*n}")
# table_print(5)   
# table_print(4)
# table_print(7,)     


# def sub(a,b): # parameter
#     c = a-b
#     print(c)
    
# sub(20,50) #arguments 



# def mul(a,b): # parameter
#     c = a*b
#     print(c)
    
# mul(4,7) #arguments 


# def dev(a,b): # parameter
#     c = a%b
#     print(c)
    
# dev(20,2) #arguments 



# we can do this thing in conditional way 


# def add(a,b):
#     c =a+b
#     print("add :", a+b)
# def sub(a,b): # parameter
#     print("sub :", a-b)
# def mul(a,b): # parameter:
#     print("mil :",a*b)
# def dev(a,b): # parameter
#     print("dev :",a/b)
# while True:    
#     num1 = int(input("enter your number"))
#     num2 = int(input("enter your 2nd number"))
#     opt = input("select '+' , '-' , '*' , '/' and '0' for stop the program")
#     if opt =="-":
#         sub(num1,num2)
#     elif opt =="/" :
#         dev(num1,num2)
#     elif opt == "*":
#         mul(num1,num2)
#     elif opt =="+" :
#         add(num1,num2)    
#     elif opt == 0:
#         print("program is closed")           
        
        
        
        
def add(a,b):
    return a+b
res = add(20,5)

def sub(a,c):
    return a-c
print(10-res)  

