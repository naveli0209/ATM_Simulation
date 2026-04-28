from check_balance import check_balance
from deposit import deposit
from show_statement import show_statement
from withdraw  import withdraw

def atm():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice==1:   check_balance()
        elif choice==2: deposit()
        elif choice==3: withdraw()
        elif choice==4: show_statement()
        elif choice==5: 
            print("Thank you")
            break
        else:
            print("Invalid choice")
            
atm()