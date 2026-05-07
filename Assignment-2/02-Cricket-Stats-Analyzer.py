player1 = int(input("Enter the runs scored by player 1:"))
player2 = int(input("Enter the runs scored by player 2:"))  
player3 = int(input("Enter the runs scored by player 3:"))
player4 = int(input("Enter the runs scored by player 4:"))
player5 = int(input("Enter the runs scored by player 5:"))

total = player1 + player2 + player3 + player4 + player5
avg = total / 5
print(f"{'-'*40}\nThe total runs scored by the team is: {total} \n The average runs scored by the team is: {avg} \n{'-'*40}")