
# ATM Transaction Sequence Simulation

# Initial account details
balance = float(input("Enter initial account balance: "))
withdrawal_limit = 10000

# Transaction counters
total_deposits = 0
total_withdrawals = 0
rejected_transactions = 0

# Transaction count
n = int(input("Enter number of transactions: "))

for i in range(n):

    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdraw")

    choice = input("Enter transaction type (1/2): ")
    amount = float(input("Enter transaction amount: "))

    # Validate transaction amount
    if amount <= 0:
        print("Rejected: Invalid transaction amount.")
        rejected_transactions += 1

    # Deposit transaction
    elif choice == '1':
        balance += amount
        total_deposits += amount
        print("Deposit successful.")
        print("Current balance:", balance)

    # Withdrawal transaction
    elif choice == '2':

        if amount > withdrawal_limit:
            print("Rejected: Withdrawal limit exceeded.")
            rejected_transactions += 1

        elif amount > balance:
            print("Rejected: Insufficient balance.")
            rejected_transactions += 1

        else:
            balance -= amount
            total_withdrawals += amount
            print("Withdrawal successful.")
            print("Current balance:", balance)

    # Invalid transaction type
    else:
        print("Rejected: Invalid transaction type.")
        rejected_transactions += 1

# Transaction summary
print("\n========== ATM TRANSACTION SUMMARY ==========")
print("Total Deposits       :", total_deposits)
print("Total Withdrawals    :", total_withdrawals)
print("Rejected Transactions:", rejected_transactions)
print("Final Account Balance:", balance)
print("=============================================")

