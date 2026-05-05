convert = input("Enter True or False: ").strip().lower()

if convert == "true":
    convert = True
elif convert == "false":
    convert = False
else:
    print("Invalid input")
    exit()

print(f"You entered: {convert} (type: {type(convert)})")

print(1 if convert else 0)
