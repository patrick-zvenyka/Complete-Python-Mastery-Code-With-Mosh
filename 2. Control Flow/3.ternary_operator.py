# Student applying for university
from pyexpat.errors import messages

# simple way of writing code
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# clean way of writing code
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "not Eligible"

print(message)

# cleaner way of writing code
age = 16
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

