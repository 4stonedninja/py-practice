# Simulated webhook payload (like Stripe, Razorpay, etc.)

webhook_payload = {
    "event": "payment_success",
    "user": {
        "id": 101,
        "name": "Hemanshu"
    },
    "amount": 499,
    "currency": "INR",
    "status_code": 200
}



# Accessing data

event = webhook_payload["event"]
user_name = webhook_payload["user"]["name"]
amount = webhook_payload["amount"]
status_code = webhook_payload["status_code"]

# Conditional logic
if status_code == 200:
    print(f"payment successful for {user_name}")
    print(f"Amount: {amount} {webhook_payload['currency']}")
elif status_code == 400:
    print("Bad request")
else:
    print("Unknown webhook status")