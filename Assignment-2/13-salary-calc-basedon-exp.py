exp = int(input("Enter your years of experience: "))
if exp >=15:
    bonus = 5000
    salary = 80000
    final_salary = salary + bonus

    print(f"{"-"*45}\nYou are a senior employee and your salary is {salary}\n and your bonus is {bonus}.\n Your final salary is {final_salary}.\n{"-"*45}")

elif exp >= 10 and exp < 15:
    salary = 80000
    bonus = 0
    final_salary = salary + bonus
    print(f"{"-"*45}\nYou are a senior employee with salary of {salary}\n and bonus of {bonus}\n your final salary is {final_salary}.\n{"-"*45}")
elif exp >= 5 and exp < 9:
    salary = 50000
    bonus = 0
    final_salary = salary + bonus
    print(f"{"-"*45}\nYou are a mid-level employee with salary of {salary}\n and bonus of {bonus}\n your final salary is {final_salary}.\n{"-"*45}")
else:
    salary = 30000
    bonus = 0
    final_salary = salary + bonus
    print(f"{"-"*45}\nYou are a junior employee with salary {salary}\n and bonus of {bonus}\n your final salary is {final_salary}.\n{"-"*45}")