import upskill_python.client as client


class Bank:
    def __init__(self):
        self.client_list = list()

    def add_client(self, new_client_name, initial_balance):  # create new client instance and add it to client_list
        new_client_ID = len(self.client_list)
        new_client = client.Client(new_client_ID, new_client_name, initial_balance)
        self.client_list.append(new_client)

    def remove_client(self, name_client_to_remove):  # remove client from the client_list and remove client instance
        for index, client in enumerate(self.client_list):
            if client.name == name_client_to_remove:
                self.client_list.pop(index)
                client.__del__()
                for client in self.client_list[index:]:
                    client.ID -= 1

    def get_client(self, client_name):  # takes client_name as an argument and returns client instance
        for client in self.client_list:
            if client.name == client_name:
                return client
        raise ValueError(f"There is no client called {client_name} in the database.")

    def get_all_clients_info(
        self,
    ):  # return str containing info about all clients in the bank
        message = ""
        for client in self.client_list:
            message += f"{client.ID} \t {client.name} \t {client.balance} \n"
        return message

    def get_client_transactions(self, client_name):  # takes client instance and returns transaction history
        for some_client in self.client_list:
            if some_client.name == client_name:
                return some_client.get_transaction_history()
        raise ValueError("No such client in the database")
