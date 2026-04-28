from utils import transactions

def show_statement():
    print("\n--- Transaction History ---")

    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(f"{t['type']} - ₹{t['amount']}")