age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income: "))
creadit_score = float(input("Enter your credit score: "))
outstanding_debt = float(input("Enter your outstanding debt: "))

if age >= 18 and monthly_income > 25000 and creadit_score > 700 and outstanding_debt <= 10000:
    print("Congratulations! Your loan application has been approved.")
else:
    print("Sorry, your loan application has been rejected.") 
