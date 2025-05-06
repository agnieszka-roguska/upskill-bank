import pytest

import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import upskill_python.bank as bank
import upskill_python.client as client
import upskill_python.transaction as transaction

@pytest.fixture
def my_bank():
    bank_inst = bank.Bank()
    bank_inst.add_client("John Doe", 100)
    return bank_inst

@pytest.fixture
def random_client():
    return client.Client("John Doe", 100)

@pytest.fixture
def another_client():
    return client.Client("John Cena", 5000000)

##############################################################################
class TestBankClass:
    def test_bank_instance_initialization(self, my_bank, random_client):
        assert my_bank.client_list == [random_client]

    def test_adding_new_client_bank_class(self, my_bank, another_client):
        my_bank.add_client(another_client.name, another_client.balance)
        assert len(my_bank.client_list) == 2
        assert another_client in my_bank.client_list
        assert my_bank.client_list[1].name == another_client.name
        assert my_bank.client_list[1].id != ""
    
    def test_get_client_bank_class(self, my_bank, random_client):
        get_client = my_bank.get_client("John Doe")
        assert get_client == random_client

    def test_get_client_not_in_the_database_error_bank_class(self, my_bank, random_client):
        incorrect_name = "Johnanna Doe"
        with pytest.raises(ValueError) as excinfo:
            get_client = my_bank.get_client(incorrect_name)
        assert str(excinfo.value) == f"There is no client called {incorrect_name} in the database."

    def test_remove_client_bank_class(self, my_bank, random_client):
        my_bank.remove_client(random_client.name)
        assert my_bank.client_list == []

    def test_remove_client_invalid_client_name_bank_class(self, my_bank):
        with pytest.raises(ValueError) as excinfo:
            my_bank.remove_client("Johanna Doe")
        assert str(excinfo.value) == "There is no such client in the database"
        
    def test_get_all_client_balances_bank_class(self, my_bank, random_client):
        info = f"{random_client.name} \t {random_client.balance} \n"
        result = my_bank.get_all_client_balances()
        assert result == info

##############################################################################
class TestClientClass:
    @pytest.mark.parametrize(
            "random_name, random_initial_balance",
            [
                ("Random Name 1", 333),
                ("Random Name 2", -13.0),
                ("Random Name 3", 1010)
            ]
    )
    def test_client_instance_initialization(self, random_name, random_initial_balance):
        new_client = client.Client(random_name, random_initial_balance)
        assert new_client.name == random_name
        assert new_client.balance == random_initial_balance
        assert new_client.id != ""

    def test_dunder_str_function_client_class(self, random_client):
        expected_message = f"Name: John Doe\t Client ID: {random_client.id} Balance: 100"
        assert str(random_client) == expected_message
    
    def test_dunder_repr_function_client_class(self, random_client):
        expected_message = f"Client({random_client.name}, {random_client.balance})"
        assert repr(random_client) == expected_message

    @pytest.mark.parametrize(
            "amount_to_depose, expected_balance, expected_exception",
            [(230, 330, None), 
             (0, 100, None), 
             (11, 111, None), 
             (500, 600, None), 
             (99, 199, None), 
             (-200, 199, ValueError)
             ],
    )
    def test_depose_client_class(self, random_client, amount_to_depose, expected_balance, expected_exception):
            if expected_exception:
                with pytest.raises(expected_exception) as excinfo:
                    random_client.depose(amount_to_depose)
                assert str(excinfo.value) == "The amount can't be negative"
            else: 
                random_client.depose(amount_to_depose)
                assert random_client.balance == expected_balance            
    @pytest.mark.parametrize(
                "amount_to_withdraw, expected_balance, expected_exception",
                [
                (50, 50, None),
                (100, 0, None),
                (1, 99, None),
                (101, 100, ValueError),
                (-1, 100, ValueError)
                ],
            )
    def test_withdraw_client_class(self, random_client, amount_to_withdraw, expected_balance, expected_exception):
        if expected_exception:
            with pytest.raises(expected_exception) as excinfo:
                random_client.withdraw(amount_to_withdraw)
            if amount_to_withdraw < 0:
                assert str(excinfo.value) == "The amount can't be negative"
            else: 
                assert str(excinfo.value) == f"Transaction declined due to insufficient funds. Your account balance is {random_client.balance}. Failed transation info: withdraw, {amount_to_withdraw}"
        else:
            random_client.withdraw(amount_to_withdraw)
            assert random_client.balance == expected_balance

    def test_get_transaction_history_when_no_transactions_client_class(self, random_client):
        transaction_history = random_client.get_transaction_history()
        expected_message = "No history"
        assert transaction_history == expected_message

    def test_get_transaction_history_client_class(self, random_client):
        amount_to_withdraw = 23
        random_client.withdraw(amount_to_withdraw)
        message_1 = f"Client: {random_client.name} \tTransaction type: withdraw \tTransaction ID: {random_client.transaction_list[0].id} \tTransaction amount: -23 \tTransaction date: {random_client.transaction_list[0].transaction_date} \tBalance after operation: {random_client.transaction_list[0].balance_after_operation}\n"
        amount_to_depose = 100
        random_client.depose(amount_to_depose)
        message_2 = f"Client: {random_client.name} \tTransaction type: deposit \tTransaction ID: {random_client.transaction_list[1].id} \tTransaction amount: 100 \tTransaction date: {random_client.transaction_list[1].transaction_date} \tBalance after operation: {random_client.transaction_list[1].balance_after_operation}\n"
        expected_transaction_history = f"Here is the transaction history for {random_client.name}:\n" + message_1 + message_2
        transaction_history = random_client.get_transaction_history()
        assert transaction_history == expected_transaction_history

##############################################################################
class TestTrancationClass:
    @pytest.mark.parametrize(
            "client_data, expected_exception",
            [
                ({
                "name" : "John Doe",
                "transaction_type" : "wITHdRaW",
                "transaction_amount" : 16,
                "balance_after_operation" : 32
                },
                None),
                ({
                "name" : "John Doe",
                "transaction_type" : "wITHdRaW",
                "transaction_amount" : 0,
                "balance_after_operation" : 0
                },
                None),
                ({
                "name" : "John Doe",
                "transaction_type" : "withdraw",
                "transaction_amount" : -1,
                "balance_after_operation" : 100
                }, 
                ValueError),
                ({
                "name" : "John Doe",
                "transaction_type" : "incorrect_transaction_type",
                "transaction_amount" : 1,
                "balance_after_operation" : 100
                }, 
                ValueError)
            ]
    )
    def test_transaction_instance_initialization_withdraw(self, client_data, expected_exception):
        if expected_exception:
            with pytest.raises(expected_exception) as excinfo:
                    new_transaction = transaction.Transaction(client_data["name"], client_data["transaction_type"], client_data["transaction_amount"], client_data["balance_after_operation"])
            if client_data["transaction_amount"] < 0:
                assert str(excinfo.value) == "Transaction amount can't be a negative number."
            else: 
                assert str(excinfo.value) == "Invalid transaction type"
        else: 
            new_transaction = transaction.Transaction(client_data["name"], client_data["transaction_type"], client_data["transaction_amount"], client_data["balance_after_operation"])
            assert new_transaction.client_name == client_data["name"]
            assert new_transaction.transaction_type == client_data["transaction_type"].lower()
            assert new_transaction.transaction_amount == -client_data["transaction_amount"]
            assert new_transaction.id != ""
            assert new_transaction.balance_after_operation == client_data["balance_after_operation"]

    def test_dunder_method_str_transaction_class(self):
        client_name = "John Doe"
        transaction_type = "WiTHdrAw"
        transaction_amount = 16
        balance_after_operation = 32
        new_transaction = transaction.Transaction(client_name, transaction_type, transaction_amount, balance_after_operation)
        
        assert str(new_transaction) == f"Client: {client_name} \tTransaction type: {transaction_type.lower()} \tTransaction ID: {new_transaction.id} \tTransaction amount: {-transaction_amount} \tTransaction date: {new_transaction.transaction_date} \tBalance after operation: {balance_after_operation}"