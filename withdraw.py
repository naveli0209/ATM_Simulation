from utils import account, transactions

def withdraw():
    amount = int(input("Enter amount to withdraw: "))

    if amount > account["balance"]:
        print("Insufficient Balance!")
        return

    if amount <= 0:
        print("Invalid amount!")
        return

    account["balance"] -= amount

    transactions.append({
        "type": "Withdraw",
        "amount": amount
    })

    print("Withdrawal Successful!")