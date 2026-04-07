age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    if age >=65:
        print("you are a senior citizen")
elif age < 0:
    print("The number you entered is not a Age")
else:
    print("You are not able to vote. ")