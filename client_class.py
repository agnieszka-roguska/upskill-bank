from datetime import datetime
import transaction_class
import tests

class Client:
    def __init__(self, ID, name, balance):
        self.ID = ID
        self.name = name
        self.balance = balance
        self.transaction_list = []
    
    def __str__(self):
        print(f"Client info:")
        print("\t Name: ", self.name, "\t Client ID: ", self.__ID, "\t Balance: ", self.balance)
    
    def __repr__(self):
        return f"Client({self.ID}, {self.name}, {self.balance})"

    def __eq__(self, another_client):
        return self.ID == another_client.ID and self.name == another_client.name and self.balance == another_client.balance

    def depose(self, amount):
        self.balance += amount
        transaction = transaction_class.Transaction(self.name, "deposit", amount, datetime.now(), self.get_balance())
        self.transaction_list.append(transaction)

    def withdraw(self, amount):
        transaction_name = "withdraw"
        if (self.balance >= amount) & (amount >= 0):
            self.balance -= amount
            transaction = transaction_class.Transaction(self.name, transaction_name, amount, datetime.now(), self.get_balance())
            self.transaction_list.append(transaction)
        elif amount < 0:
            raise ValueError("The amount can't be negative")
        else:
            raise ValueError(f"Transaction declined due to insufficient funds. Your account balance is {self.balance}. Failed transation info: {transaction_name}, {amount}")

    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        if len(self.transaction_list) == 0:
            return "No history"
        else: 
            message = f"Here is the transaction history for {self.name}:\n"
            for transaction in self.transaction_list:
                message += f"Date: {transaction.transaction_date}\t Type: {transaction.transaction_type}\t Amount: {transaction.transaction_amount}\t Account balance after the transaction: {transaction.balance_after_operation}\n"
            return message