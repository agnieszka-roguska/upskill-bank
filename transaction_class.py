class Transaction:
    def __init__(self, client_name, transaction_type, transaction_amount, transaction_date, balance_after_operation):
        if transaction_type.lower() not in ["deposit", "withdraw"]:
            raise ValueError("Invalid transaction type")
        elif transaction_amount < 0:
            raise ValueError("Transaction amount can't be a negative number.")
        
        if transaction_type == "withdraw":
            transaction_amount = -transaction_amount

        self.client_name = client_name
        self.transaction_type = transaction_type.lower()
        self.transaction_amount = transaction_amount
        self.transaction_date = transaction_date
        self.balance_after_operation = balance_after_operation

    def __str__(self):
        message = f"Transaction details: \n \tClient name: {self.client_name} \tTransaction type: {self.transaction_type} \tTransaction amount: {self.transaction_amount} \tTransaction date: {self.transaction_date} \tBalance after operation: {self.balance_after_operation}"
        return message