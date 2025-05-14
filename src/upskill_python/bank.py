import upskill_python.client as client


class Bank:
    def __init__(self):
        self.client_list: list[client.Client] = []

    def add_client(self, new_client_name: str, initial_balance: int | float) -> None:
        """Create new client instance and add it to the client_list."""
        new_client = client.Client(new_client_name, initial_balance)
        self.client_list.append(new_client)

    def remove_client(self, name_client_to_remove: str) -> None:
        if not any(some_client.name == name_client_to_remove for some_client in self.client_list):
            raise ValueError("There is no such client in the database")
        else:
            for index, some_client in enumerate(self.client_list):
                if some_client.name == name_client_to_remove:
                    self.client_list.pop(index)

    def get_client(
        self, client_name: str
    ) -> client.Client:  # takes client_name as an argument and returns client instance
        for some_client in self.client_list:
            if some_client.name == client_name:
                return some_client
        raise ValueError(f"There is no client called {client_name} in the database.")

    def get_all_client_balances(self) -> str:
        """return str containing info about all clients and their balances"""
        message = ""
        for some_client in self.client_list:
            message += f"{some_client.name} \t {some_client.balance} \n"
        return message
