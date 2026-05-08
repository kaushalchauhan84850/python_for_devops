cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))


if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You make a profit of: {profit}")
    print(f"Profit percentage: {(profit / cost_price) * 100}%")
    
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"You incur a loss of: {loss}")
    print(f"Loss percentage: {(loss / cost_price) * 100}%")
else:
    print("No profit, no loss.")