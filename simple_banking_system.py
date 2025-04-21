import client_class
import transaction_class
import bank_class

if __name__ == '__main__':
    my_bank = bank_class.Bank()
    my_bank.add_client("Agnieszka Roguska", 0)
    my_bank.add_client("Franek Kimono", 10)
    my_bank.add_client("Juliusz Cezar", 60)
    my_bank.add_client("Patrycjusz Gąbka", 670)
    my_bank.add_client("Żwirek i Muchomorek", 230)
    my_bank.add_client("Joachim Wielki", 1)
    print(my_bank.get_all_clients_info())
    my_bank.remove_client("Patrycjusz Gąbka")
    print(my_bank.get_all_clients_info())

