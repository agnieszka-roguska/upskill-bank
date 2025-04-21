import pytest
import bank_class
import client_class


@pytest.fixture
def bank():
    bank_inst = bank_class.Bank()
    bank_inst.add_client("John Doe", 100)
    return bank_inst


@pytest.fixture
def client():
    return client_class.Client(0, "John Doe", 100)


@pytest.fixture
def another_client():
    return client_class.Client(1, "John Cena", 5000000)


##############################################################################
class TestBankClass:
    def test_bank_instance_initialization(self, bank, client):
        assert bank.client_list == [client]

    def test_adding_new_client_bank_class(self, bank, another_client):
        bank.add_client(another_client.name, another_client.balance)
        assert another_client in bank.client_list

    def test_get_client_bank_class(self, bank, client):
        get_client = bank.get_client("John Doe")
        assert get_client == client

    def test_remove_client_bank_class(self, bank, client):
        bank.remove_client(client.name)
        assert len(bank.client_list) == 0

    def test_get_all_clients_info_bank_class(self, bank, client):
        info = f"{client.ID} \t {client.name} \t {client.balance} \n"
        result = bank.get_all_clients_info()
        assert result == info

    def test_get_client_transactions_bank_class(self):
        pass


##############################################################################
class TestClientClass:
    def test_client_instance_initialization(self, client):
        pass

    def test_dunder_str_function_client_class(self):
        pass

    def test_depose_client_class(self):
        pass

    def test_withdraw_client_class(self):
        pass

    def test_get_balance_client_class(self):
        pass

    def test_print_statemenet_client_class(self):
        pass


##############################################################################
class TestTrancationClass:
    def test_transaction_instance_initialization(self):
        pass
