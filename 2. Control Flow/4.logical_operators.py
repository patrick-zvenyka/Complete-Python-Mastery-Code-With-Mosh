# Processing loan
from xml.sax.handler import property_interning_dict

high_income = True
good_credit = True
student = False

# and logical operator
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# or logical operator
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# not logical operator
if not student:
    print("Eligible")
else:
    print("Not Eligible")

# complex conditions
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")