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
print(encode("xyz", 3))  # Output (['a', 'b', ..., 'z'], 'abc')
print(encode("j!K,2?", 3))  # Output  (['a', 'b', ..., 'z'], 'm!n,2?') 
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

# Example usage:
print(decode("abc", 3))  
import datetime

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date if creation_date else datetime.date.today()
        self.balance = balance
        if self.creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def view_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if (datetime.date.today() - self.creation_date).days < 180:
            raise Exception("Withdrawals only permitted after 180 days.")
        super().withdraw(amount)
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount)
        if self.balance < 0:
            self.balance -= 30  # Apply overdraft fee
            print(f"Overdraft fee applied. New balance: {self.balance}")
