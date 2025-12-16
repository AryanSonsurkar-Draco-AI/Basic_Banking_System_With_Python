import json
import os

if not os.path.exists("bank_data.json"):
    with open("bank_data.json", "w") as file:
        json.dump({"accounts": {}}, file, indent=4)

import json

def create_account():
    acc = input("Please enter your account no. (ex. 200925): ").strip()
    name = input("Enter your name: ").strip()
    
    try:
        deposit = float(input("Enter amount to deposit or 0 if you don't want to deposit: "))
    except ValueError:
        print("Invalid amount.")
        return

    if not acc or not name:
        print("Account number and name cannot be empty.")
        return

    if deposit < 0:
        print("Deposit cannot be negative.")
        return

    with open("bank_data.json", "r") as file:
        data = json.load(file)

    accounts = data["accounts"]

    if acc in accounts:
        print("Account already exists.")
        return

    accounts[acc] = {
        "name": name,
        "balance": deposit
    }

    with open("bank_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Account created successfully!")

def deposit_money():
    acc = input("Enter account number: ").strip()

    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than 0.")
        return

    with open("bank_data.json", "r") as file:
        data = json.load(file)

    accounts = data["accounts"]

    if acc not in accounts:
        print("Account not found.")
        return

    accounts[acc]["balance"] += amount

    with open("bank_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Deposit successful. New balance: {accounts[acc]['balance']}")

def withdraw_money():
    acc = input("Enter account number: ").strip()

    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Withdraw amount must be greater than 0.")
        return

    with open("bank_data.json", "r") as file:
        data = json.load(file)

    accounts = data["accounts"]

    if acc not in accounts:
        print("Account not found.")
        return

    if accounts[acc]["balance"] < amount:
        print("Insufficient balance.")
        return

    accounts[acc]["balance"] -= amount

    with open("bank_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Withdrawal successful. Remaining balance: {accounts[acc]['balance']}")

def check_balance():
    acc = input("Enter account number: ").strip()

    with open("bank_data.json", "r") as file:
        data = json.load(file)

    accounts = data["accounts"]

    if acc not in accounts:
        print("Account not found.")
        return

    print("Account Holder:", accounts[acc]["name"])
    print("Current Balance:", accounts[acc]["balance"])

def main_menu():
    while True:
        print("\n===== BASIC BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using the Banking System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__=="__main__":
    main_menu()