import pytest

import sys
import os
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
        in_list: bool = another_client in my_bank.client_list
        compare_names: bool = my_bank.client_list[1].name == another_client.name
        id_not_empty: bool = my_bank.client_list[1].id != 0
        assert in_list & compare_names & id_not_empty
    
    def test_get_client_bank_class(self, my_bank, random_client):
        get_client = my_bank.get_client("John Doe")
        assert get_client == random_client

    def test_remove_client_bank_class(self, my_bank, random_client):
        my_bank.remove_client(random_client.name)
        assert my_bank.client_list == []

    def test_get_all_client_balances_bank_class(self, my_bank, random_client):
        info = f"{random_client.name} \t {random_client.balance} \n"
        result = my_bank.get_all_client_balances()
        assert result == info

##############################################################################
class TestClientClass:
    def test_client_instance_initialization(self):
        random_name = "Random Name"
        random_initial_balance = 300
        new_client = client.Client(random_name, random_initial_balance)
        assert (new_client.name == random_name) & (new_client.balance == random_initial_balance) & (new_client.id != "")

    def test_dunder_str_function_client_class(self, random_client):
        expected_message = f"Name: John Doe\t Client ID: {random_client.id} Balance: 100"
        assert str(random_client) == expected_message
    
    def test_dunder_repr_function_client_class(self, random_client):
        expected_message = f"Client({random_client.name}, {random_client.balance})"
        assert repr(random_client) == expected_message

    def test_depose_client_class(self, random_client):
        amount_to_depose = 230
        expected_balance = random_client.balance + amount_to_depose
        random_client.depose(amount_to_depose)
        assert random_client.balance == expected_balance

    def test_withdraw_correct_inputs_client_class(self, random_client):
        amount_to_withdraw = 50
        expected_balance = random_client.balance - amount_to_withdraw
        random_client.withdraw(amount_to_withdraw)
        assert random_client.balance == expected_balance

    def test_withdraw_negative_amount_client_class(self, random_client):
        amount_to_withdraw = -1
        message = random_client.withdraw(amount_to_withdraw)
        expected_message = {"status": "ERROR", "content": "The amount can't be negative"}
        assert message == expected_message
    
    def test_withdraw_insufficient_funds_client_class(self, random_client):
        amount_to_withdtaw = 1000
        message = random_client.withdraw(amount_to_withdtaw)
        expected_message = {"status": "ERROR", "content": f"Transaction declined due to insufficient funds. Your account balance is {random_client.balance}. Failed transation info: withdraw, {amount_to_withdtaw}"}
        assert message == expected_message

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
    def test_transaction_instance_initialization(self):
        pass