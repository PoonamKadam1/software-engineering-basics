Bank_details={}
def create_account():
    name= input("Enter your name: ")
    acc_number= input("Enter your account number: ")
    initial_deposit= float(input("Enter initial deposit amount: "))
    Bank_details[acc_number] = {'Name': name, 'Balance': initial_deposit}
    print("Account created successfully!")  
def deposit():
    acc_number= input("Enter your account number: ")
    if acc_number in Bank_details:
        amount= float(input("Enter amount to deposit: "))
        total_balance=amount+ Bank_details[acc_number]['Balance']
        Bank_details[acc_number]['Balance']= total_balance
        print ("Deposited,your current balance is :", total_balance)
    else:
        print("Account not found.")
def withdraw():
    acc_number= input("Enter your account number: ")
    if acc_number in Bank_details:
        amount = float(input("Enter mount you want to withdraw:"))
        if Bank_details[acc_number]['Balance'] <= 500:
            print ("Sorry, you have minimum balance")
        else:
            total_balance=Bank_details[acc_number]['Balance']- amount
            print ("withdraw, your current balance is: ", total_balance)
    else:
        print("Account not found.")
def main():
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            acc_number = input("Enter your account number: ")
            if acc_number in Bank_details:
                print(
                    "Account Holder:",
                    Bank_details[acc_number]['Name']
                )
                print(
                    "Current Balance:",
                    Bank_details[acc_number]['Balance']
                )
            else:
                print("Account not found.")

        elif choice == "5":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()