from uuid import uuid4
from datetime import datetime
import upskill_python.transaction as transaction

class Client:
    def __init__(self, name: str, balance: int | float) -> None:
        self.__id = uuid4().hex
        self.name = name
        self.__balance = balance
        self.transaction_list = []

    def __str__(self) -> None:
        message = f"Name: {self.name}\t Client ID: {self.id} Balance: {self.balance}"
        return message
    
    def __repr__(self) -> str:
        return f"Client({self.name}, {self.balance})"

    def __eq__(self, another_client: 'Client') -> bool:
        return self.balance == another_client.balance and self.name == another_client.name
    
    @property
    def id(self) -> str:
        return self.__id
    
    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: int | float) -> None:
        self.__balance = value

    def depose(self, amount: int | float) -> None:
        transaction_name = transaction.TransactionType.DEPOSIT.value
        if amount >= 0:
            self.balance = self.balance + amount
        else:
            raise ValueError("The amount can't be negative")
        new_transaction = transaction.Transaction(self.name, transaction_name, amount, self.balance)
        self.transaction_list.append(new_transaction)

    def withdraw(self, amount: int | float) -> None:
        transaction_name = transaction.TransactionType.WITHDRAW.value #"withdraw"
        if (self.balance >= amount) & (amount >= 0):
            self.balance = self.balance - amount
            new_transaction = transaction.Transaction(self.name, transaction_name, amount, self.balance)
            self.transaction_list.append(new_transaction)
        elif amount < 0:
            raise ValueError("The amount can't be negative")
        else:
            raise ValueError(f"Transaction declined due to insufficient funds. Your account balance is {self.balance}. Failed transation info: {transaction_name}, {amount}")
    
    def get_transaction_history(self) -> str:
        if len(self.transaction_list) == 0:
            return "No history"
        else: 
            message = f"Here is the transaction history for {self.name}:\n"
            for some_transaction in self.transaction_list:
                message += str(some_transaction) + "\n"
            return message