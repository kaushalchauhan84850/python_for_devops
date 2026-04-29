print("hii i am your calculator")
task = input("what do you want to do? (add, subtract, multiply, divide): ")

if task == "add":
    num1 = float(input("enter your number to add:"))
    num2 =float(input("enter your second number to add:"))
    result = num1 + num2
    print("your added value is:" , result)
 
elif task == "subtract":
    num1 = float(input("enter your first number to subtract:"))
    num2 = float(input("enter your second number to subtract:"))
    result = num1 - num2
    print("your subtrated value is:"  , result)
    
elif task == "multiply":
    num1 = float(input("enter your first number to multiply:"))
    num2 = float(input("enter your second number to multiply:"))
    result = num1 * num2
    print("your multiplied value is:" , result)
    
elif task == "divide":
    num1 = float(input("enter your first number to divide:"))
    num2 = float(input("enter your second number to divide:"))
    if num2 != 0:
        result = num1 / num2
        print("your divided value is:" , result)
    else:
        print("Error: Cannot divide by zero.")
    
