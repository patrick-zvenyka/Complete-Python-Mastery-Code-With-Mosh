try:
    file = open('cleaning_up.py')
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid age provided.")
    
else:
    print("File and age processed successfully.")

finally:
    file.close()