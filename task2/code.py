initial_balance = float(input("Enter initial balance: "))
withdrawal_limit = float(input("Enter withdrawal limit: "))

transactions = [
    ("deposit", 2000),
    ("withdrawal", 1000),
    ("withdrawal", 5000),
    ("deposit", 0),
    ("withdrawal", 500)
]

successful_transactions = 0
rejected_transactions = 0

for transaction_type, amount in transactions:
    print("\nTransaction:", transaction_type, amount)

    if amount <= 0:
        print("Transaction rejected: Invalid amount")
        rejected_transactions += 1

    elif transaction_type == "deposit":
        initial_balance += amount
        successful_transactions += 1
        print("Deposit successful")

    elif transaction_type == "withdrawal":
        if amount <= initial_balance and amount <= withdrawal_limit:
            initial_balance -= amount
            successful_transactions += 1
            print("Withdrawal successful")
        else:
            print("Transaction rejected: Limit or balance exceeded")
            rejected_transactions += 1

    else:
        print("Transaction rejected: Invalid transaction type")
        rejected_transactions += 1

print("\n----- TRANSACTION SUMMARY -----")
print("Successful transactions:", successful_transactions)
print("Rejected transactions:", rejected_transactions)
print("Final account balance:", round(initial_balance, 2))
