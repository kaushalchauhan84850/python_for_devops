x = input("Enter your choice: ")
if isinstance(x, int):
    print(f"{x} is an integer.")
else:
    print(f"{x} is not an integer.")
    
print("but after conversion:")
y = int(x)
if isinstance(y, int):
    print(f"{y} is an integer.")
else:
    print(f"{y} is not an integer.")
