
import re

# Date validation
date = input("Enter date (DD/MM/YYYY): ")
date_pattern = r'^\d{2}/\d{2}/\d{4}$'

if re.fullmatch(date_pattern, date):
    print("Given valid date")
else:
    print("Invalid date")

# Email and mobile number validation
data = input("Enter email or phone number: ")

email_pattern = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^[0-9]{10}$'

if re.fullmatch(email_pattern, data):
    print("Valid email ID")
elif re.fullmatch(mobile_pattern, data):
    print("Valid mobile number")
else:
    print("Invalid email ID or Invalid mobile number")

