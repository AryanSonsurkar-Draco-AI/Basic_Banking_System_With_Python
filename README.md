Basic Banking System (Python + JSON)

A simple command-line based banking system built using Python that supports account creation, deposits, withdrawals, and balance checking. All data is stored persistently using a JSON file.

Features

Create a new bank account

Deposit money into an existing account

Withdraw money with balance validation

Check account balance and account holder name

Persistent storage using a JSON file

Menu-driven CLI interface

Input validation and error handling

Project Structure

├── banking_system.py
├── bank_data.json
└── README.md


banking_system.py
Contains all banking logic and menu handling.

bank_data.json
Stores all account data persistently.

JSON Data Format

The data is stored in the following structure:

{
    "accounts": {
        "ACCOUNT_NUMBER": {
            "name": "Account Holder Name",
            "balance": 0.0
        }
    }
}


Each account number acts as a unique key.

How It Works

On startup, the program checks if bank_data.json exists.

If the file does not exist, it is automatically created.

Users interact with the system through a menu.

All changes (create, deposit, withdraw) are saved immediately to the JSON file.

Usage

Clone or download the repository.

Run the program using Python:

python banking_system.py


Choose an option from the menu:

Create Account

Deposit Money

Withdraw Money

Check Balance

Exit

Validation Rules

Account numbers must be unique.

Deposit and withdrawal amounts must be greater than zero.

Withdrawals cannot exceed available balance.

Account number and name cannot be empty.

Technologies Used

Python 3

JSON for data storage

Standard Python libraries (json, os)

Possible Improvements

Add PIN authentication

Transaction history

Interest calculation

Object-Oriented version

Account deletion feature

Author

Aryan Sonsurkar
First-year Computer Engineering student