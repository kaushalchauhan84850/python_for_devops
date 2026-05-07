age = int(input("Please enter your current age: "))
retirement_age = 65 - age
if retirement_age >= 1:
    print(f"You have {retirement_age} years left until you can retire.")
else:
    print("Congratulations! You are already eligible for retirement.") 