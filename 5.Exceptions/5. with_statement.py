try:
    with open('cleaning_up.py') as file:
        print("File opened successfully.")
        file.__
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid age provided.")
    
else:
    print("File and age processed successfully.")

# No need for finally block to close the file, as 'with' handles it automatically.
