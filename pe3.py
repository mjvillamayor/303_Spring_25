# Functions
# A. Create an encoding function called encode
import datetime
import string


def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    shifted_text = ''
    for char in input_text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % 26
            shifted_text += alphabet[new_index]
        else:
            shifted_text += char
    return (alphabet, shifted_text)

# B. Create a decoding function called decode


def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded_text = ''
    for char in input_text:
        if char in alphabet:
            new_index = (alphabet.index(char) - shift) % 26
            decoded_text += alphabet[new_index]
        else:
            decoded_text += char
    return decoded_text


# Classes
# A. Create a class called BankAccount


class BankAccount():
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date if creation_date else datetime.date.today()
        self.balance = balance
        if self.creation_date > datetime.date.today():
            raise Exception("Creation date cannot be a future date.")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Negative deposit amount not allowed.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Negative withdrawal amount not allowed.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def view_balance(self):
        return self.balance

# B. Create a subclass of BankAccount called SavingsAccount


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if (datetime.date.today() - self.creation_date).days < 180:
            raise Exception("Withdrawals permitted after 180 days only.")
        if withdraw(amount) >= 0:
            super().withdraw(amount)
        else:
            raise ValueError("Negative account balance is not permitted.")


# C. Create a subclass of BankAccount called CheckingAccount
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount)
        if self.balance < 0:
            self.balance -= 30
            print(f"Overdraft fee applied. New balance: {self.balance}")
