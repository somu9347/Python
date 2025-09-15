age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible to apply for a driving license.")
    else:
        print("But not eligible for a driving license.")
else:
    print("You are not eligible to vote or drive.")