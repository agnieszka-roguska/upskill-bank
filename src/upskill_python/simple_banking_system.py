import client as client
import transaction as transaction
import bank as bank

import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

bank_instance = bank.Bank()

def existing_client_window():
    def change_balance_window():
        def deposit():
            client_name = entry_client.get()
            amount = float(entry_amount.get())
            try: 
                client = bank_instance.get_client(client_name)
                client.depose(amount)
                messagebox.showinfo(title = "Operation completed", message = f"{client_name} account was deposed. Current balance: {client.balance}", parent = new_window)
                new_window.destroy()
            except ValueError as e:
                messagebox.showinfo(title = f"Operation failed.", message = f"{e}", parent = new_window)
                new_window.destroy()
        
        def withdraw():
            client_name = entry_client.get()
            amount = float(entry_amount.get())
            try: 
                client = bank_instance.get_client(client_name)
                client.withdraw(amount)
                messagebox.showinfo(title = "Operation completed", message = f"{client_name} account was withdrawn. Current balance: {client.balance}", parent = new_window)
                new_window.destroy()
            except ValueError as e:
                messagebox.showinfo(title = f"Operation failed.", message = f"{e}", parent = new_window)
                new_window.destroy()
        
        
        new_window = tk.Toplevel(root)
        new_window.title("Change balance")

        tk.Label(new_window, text="Amount: ", fg = "white", bg = "black").pack()
        entry_amount = tk.Entry(new_window)
        entry_amount.pack()

        tk.Button(new_window, text="Deposit", command = deposit).pack(side = tk.LEFT)
        tk.Button(new_window, text="Withdraw", command = withdraw).pack(side = tk.RIGHT)

    def get_client_info():
        client_name = entry_client.get()
        try:
            client = bank_instance.get_client(client_name)
            messagebox.showinfo(message = str(client), parent = new_client_window)
        except ValueError as e:
            messagebox.showinfo(title = "Error", message = f"{e}", parent = new_client_window)

    def get_transaction_history():
        def destroy():
            pop_up_info_window.destroy()

        client_name = entry_client.get()
        try:
            client = bank_instance.get_client(client_name)
            message = str(client) + "\n" + client.get_transaction_history()
            pop_up_info_window = tk.Toplevel(new_client_window)
            pop_up_info_window.title("Transaction history")
            pop_up_info_window['background'] = "#9DC183"
            tk.Label(pop_up_info_window, text = message, fg = "black", bg = "#9DC183").pack()
            tk.Button(pop_up_info_window, text="OK", command = destroy).pack(side = tk.BOTTOM)
        except ValueError as e:
            messagebox.showinfo(title = "Error", message = f"{e}", parent = new_client_window)

    def remove_client():
        client_name = entry_client.get()
        try:
            bank_instance.remove_client(client_name)
            messagebox.showinfo(message = f"{client_name} was removed successfully!", parent = new_client_window)
            new_client_window.destroy()
            label.config(text = "Number of clients in the bank: " + str(len(bank_instance.client_list)))
        except ValueError as e:
            messagebox.showinfo(title = "Error", message = f"{e}", parent = new_client_window)
            new_client_window.destroy()

    new_client_window = tk.Toplevel(root)
    tk.Label(new_client_window, text="Client Name", fg = "white", bg = "black").pack()
    entry_client = tk.Entry(new_client_window)
    entry_client.pack()

    tk.Button(new_client_window, text = "Get full info", command = get_client_info).pack()
    tk.Button(new_client_window, text = "Change clients's balance", command = change_balance_window).pack()
    tk.Button(new_client_window, text = "Get client's transaction history", command = get_transaction_history).pack()
    tk.Button(new_client_window, text = "Remove Client", command=remove_client).pack()

def show_all_clients():
    messagebox.showinfo(message = bank_instance.get_all_client_balances(), parent = root)

def add_client_window():
    def add_client():
        try:
            client_name = entry_client_name.get()
            initial_balance = float(entry_amount.get())
            bank_instance.add_client(client_name, initial_balance)
            messagebox.showinfo("Add client", f"{client_name} was added successfully!", parent = new_window)
            label.config(text = "Number of clients in the bank: " + str(len(bank_instance.client_list)))
            new_window.destroy()
        except ValueError as e:
            messagebox.showinfo(title = "Error", message = f"{e} - Incorrect value entered. Try again.", parent = new_window)

    new_window = tk.Toplevel(root)
    new_window.title("Add new client")
    new_window.geometry("300x200")
    new_window['background'] = "#9DC183"

    tk.Label(new_window, text="Client Name", fg = "white", bg = "black").pack()
    entry_client_name = tk.Entry(new_window)
    entry_client_name.pack()

    tk.Label(new_window, text="Initial balance", fg = "white", bg = "black").pack()
    entry_amount = tk.Entry(new_window)
    entry_amount.pack()
    tk.Button(new_window, text="Add Client", command=add_client).pack()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Simple Banking System")
    root.geometry("700x700")
    root.resizable(False, False)
    root['background'] = "#9DC183"
    tk.Label(root, text = "Welcome to your bank application!", font = ("Arial", 21, "bold"), bg = "#9DC183").pack()
    label = tk.Label(root, text = "Number of clients in the bank: " + str(len(bank_instance.client_list)), font = ("Arial", 17), bg = "#9DC183")
    label.pack(side = "top", pady = 10, fill = "x")

    add_client_button = tk.Button(root, text = "Add Client", command = add_client_window, fg = "black", bg = "#8bc34a", width = 20, height = 7)
    add_client_button.pack(padx=5, fill = "x")
    all_clients_button = tk.Button(root, text = "Show All Clients", command = show_all_clients, fg = "black", bg = "#8bc34a", width = 20, height = 7)
    all_clients_button.pack(padx=5, fill = "x")
    existing_client_button = tk.Button(root, text = "Check existing client", command = existing_client_window, fg = "black", bg = "#8bc34a", width = 20, height = 7)
    existing_client_button.pack(padx=5, fill = "x")
    
    root.mainloop()