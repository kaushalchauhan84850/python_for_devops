convert = bool(input("Enter a boolean value (True/False): "))
print(f"You entered: {convert} (type: {type(convert)})")
if convert == "True":
    print("1")
else:
    print("0")
    convert = int(convert)
    print(type(convert))
