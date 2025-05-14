from uuid import uuid4
from enum import Enum
from datetime import datetime


class TransactionType(Enum):
    WITHDRAW = "withdraw"  # -1
    DEPOSIT = "deposit"  # 1


class Transaction:
    def __init__(
        self, client_name: str, transaction_type: str, transaction_amount: float, balance_after_operation: float
    ) -> None:
        if transaction_type.lower() not in [item.value for item in TransactionType]:
            raise ValueError("Invalid transaction type")
        elif transaction_amount < 0:
            raise ValueError("Transaction amount can't be a negative number.")

        if transaction_type.lower() == TransactionType.WITHDRAW.value:
            self.transaction_amount = -transaction_amount
        else:
            self.transaction_amount = transaction_amount

        self.__id = uuid4().hex
        self.client_name = client_name
        self.transaction_type = transaction_type.lower()
        self.transaction_date = datetime.now()
        self.balance_after_operation = balance_after_operation

    @property
    def id(self) -> str:
        return self.__id

    def __str__(self) -> str:
        message = f"Client: {self.client_name} \tTransaction type: {self.transaction_type} \tTransaction ID: {self.id} \tTransaction amount: {self.transaction_amount} \tTransaction date: {self.transaction_date} \tBalance after operation: {self.balance_after_operation}"
        return message
