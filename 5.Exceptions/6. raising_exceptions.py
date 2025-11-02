def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or negative.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print("You raised a ValueError:", error)