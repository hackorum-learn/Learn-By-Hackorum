"""
This code can be used to create and editJSON objects using python.
"""

import json


transactions = [{"id": 0, "amount": 100, "currency": "USD", "status": "pending"},
                {"id": 1, "amount": 200, "currency": "USD", "status": "completed"}]

user_transactions = {"id": 0,
                    "user_id": 0,
                    "transactions": transactions}


# Edit content of the dictionary
user_transactions["user_id"] = 123  # Change user_id
user_transactions["transactions"][0]["amount"] = 150  # Change first transaction amount

# Convert to JSON string
json_string = json.dumps(user_transactions, indent=2)

# Pretty print the updated data
print(json_string)

