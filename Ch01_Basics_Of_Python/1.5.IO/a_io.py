# print and input functionge

age = input("Enter your age: ")
if age.isdigit():
    age = float(age)
    print(f"You are {age} years old")
else:
    print("Enter the age in digits")