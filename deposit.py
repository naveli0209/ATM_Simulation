
from utils import account, transactions

def deposit():
    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    account["balance"] += amount

    transactions.append({
        "type": "Deposit",
        "amount": amount
    })

    print("Deposit Successful!")