try:
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except (ValueError,ZeroDivisionError):
    print("Invalid value. Please enter a number.")

