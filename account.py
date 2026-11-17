"""
Online Banking System - Account Management Module
"""

def account_status():
    status = "Active"
    print("Account Status:", status)

def account_details(account_number="ACC1001", account_holder="Pranay", balance=5000.0):
    print("Account Number:", account_number)
    print("Account Holder:", account_holder)
    print("Account Balance:", balance)

def activate_account():
    print("Account has been activated.")

def suspend_account():
    print("Account has been suspended.")

def verify_account():
    print("Account has been verified.")

if __name__ == "__main__":
    account_status()
