# gross salary and net salary calculation
basic_salary = float(input("Enter the basic salary: "))
bonus = float(input("Enter the bonus amount: "))
tax_rate = float(input("Enter the tax rate (in percentage): "))
other_charges = float(input("Enter any other charges: "))
gross_salary = basic_salary + bonus
tax_amount = (tax_rate / 100) * gross_salary
net_salary = gross_salary - tax_amount - other_charges
print(f"{"-"*30}\nGross Salary: {gross_salary}\nTax Amount: {tax_amount}\nNet Salary: {net_salary}\n{"-"*30}")
