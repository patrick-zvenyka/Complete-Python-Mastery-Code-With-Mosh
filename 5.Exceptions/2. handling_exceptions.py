try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
        45
    elif age < 18:
        print("You are a minor.")   
    else:
        print("You are an adult.")

except ValueError as e:
    print(f"Invalid input: {e}")    

except Exception as e:
    # Catches any other unexpected errors
    print(f"Something went wrong: {e}")
