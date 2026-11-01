print("ATM TRANSACTION SIMULATION")

initial_balance = float(input("Enter initial balance: "))
withdrawal_limit = float(input("Enter withdrawal limit: "))

number_of_transactions = int(input("Enter number of transactions: "))

successful_transactions = 0
rejected_transactions = 0

for i in range(number_of_transactions):

    print("\nTransaction", i + 1)

    transaction_type = input(
        "Enter transaction type (deposit/withdrawal): "
    ).lower()

    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        rejected_transactions += 1

    elif transaction_type == "deposit":
        initial_balance += amount
        print("Deposit successful")
        successful_transactions += 1

    elif transaction_type == "withdrawal":

        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
            rejected_transactions += 1

        elif amount > initial_balance:
            print("Insufficient balance")
            rejected_transactions += 1

        else:
            initial_balance -= amount
            print("Withdrawal successful")
            successful_transactions += 1

    else:
        print("Invalid transaction type")
        rejected_transactions += 1


print("\n----- ATM TRANSACTION SUMMARY -----")

print("Final Balance:", initial_balance)
print("Successful Transactions:", successful_transactions)
print("Rejected Transactions:", rejected_transactions)

print("Thank you for using ATM")
