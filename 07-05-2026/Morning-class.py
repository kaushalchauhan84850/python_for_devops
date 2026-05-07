name = "karan"
if name :
    print("name is not empty")
    address = "delhi"
    if address:
        print(f"address is not empty and it is : {address}")
    else:
        print("address is empty")    
else:
    print("name is empty")    
    

# we can give condition in the if statement which is called nested conditional statement 

num1 = 20 
if num1 %2 ==0:
    print(f"{num1} is even")
    number = input("enter your number:")
    if len(number) ==13 and "+91" in number:
        print("this is a valid number")
    else:
        print("this is not a valid number \n it should be 10 digit and should start with +91")   
else:
    print(f"{num1} is odd") 
    