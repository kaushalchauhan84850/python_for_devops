days = int(input("Enter the number of days you have borrowed the book:"))
if days <=5:
    fine = 2
    total_fine = fine * days
    print(f"{"-"*45}\nYou have to pay a fine of {total_fine}\n for borrowing the book for {days} days.\n{"-"*45}") 
elif days >= 6 and days <= 10:
    fine = 3
    total_fine = fine * days
    print(f"{"-"*45}\nYou have to pay a fine of {total_fine}\n for borrowing the book for {days} days.\n{"-"*45}") 
elif days >= 11 and days <= 15:
    fine = 4
    total_fine = fine * days
    print(f"{"-"*45}\nYou have to pay a fine of {total_fine}\n for borrowing the book for {days} days.\n{"-"*45}") 
else:
    fine = 5
    total_fine = fine * days
    print(f"{"-"*45}\nYou have to pay a fine of {total_fine}\n for borrowing the book for {days} days.\n{"-"*45}")   