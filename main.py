from transactions import Transaction
from data_manager import load_transactions, save_transactions

transactions = load_transactions()

def add_transaction():
    try:
        amount = float(input("Enter amount: "))
        type_ = input("Type (Income/Expense): ")
        description = input("Description: ")

        transaction = Transaction(amount, type_, description)

        transactions.append(transaction.dict)

        save_transactions(transactions)

        print("Transaction added!")
                                                       #بهاره نوریان
    except ValueError:
        print(":x: Invalid input!")


def show_transactions():
    for t in transactions:
        print(t)


def calculate_balance():
    balance = 0
    for t in transactions:
        if t["type"] == "Income":
            balance += t["amount"]
        else:
            balance -= t["amount"]

    print(f"Current Balance: {balance}")


while True:
    print("\n1. Add Transaction")
    print("2. Show Transactions")
    print("3. Balance")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        show_transactions()
    elif choice == "3":
        calculate_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
