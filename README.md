# Upskill python project
### Description:
This project implements a simple banking system with three main classes: Bank, Client, and Transaction. The system allows for the creation and management of client accounts, processing client transactions, and maintaining transaction history.

A simple graphical user interface is built using Python's tkinter library to present the project's functionality.

### Project structure:
The project consists of a few parts:

 - uv.lock file: Contains information about the project dependencies and requirements. It includes the exact resolved versions installed in the project environment. This human-readable .toml file is managed by uv and should not be edited.
 - pyproject.toml: Includes basic metadata about the project, specifies dependencies, and details about the project, as well as uv configuration options.
 - .python-version: Specifies the Python version used in the project.
 - .venv: Contains the project's virtual environment.
 - bank.py: Contains the Bank class.
 - client.py: Contains the Client class.
 - transaction.py: Contains the Transaction class.
 - simple_banking_system.py: The main script that sets up the GUI and handles user interactions.

### Installation: 
To install the project, clone the repository and install the dependencies:
1. clone the repository and navigate to the project directory
    `git clone https://github.com/agnieszka-roguska/upskill-bank.git`
    `cd upskill-python`
2. install uv and the dependencies
    `pip install uv`
    `uv init`
    `uv sync`

### Usage
- run the application
    `cd src\upskill_python`
    `uv run simple_banking_system.py`

### Running tests:
1. Navigate to the project directory
2. Install pytest and run the tests
    `pip install pytest`
    ` pytest tests/tests.py`
 

### Code Overview
- simple_banking_system.py - The main script - a simple GUI app to present project functionality
- bank.py : Contains the Bank class which manages clients and their transactions
- client.py : Contains the Client class which represents a bank client.
- transaction.py : Contains the Transaction class which represents a transaction

### Bank class
The bank class manages the clients ans their transactions.

**Attributes:**
 - client_list : A list of Client instances

**Methods:**
 - __init__ : Initializes the bank with empty client list
 - add_client : Creates a new client instance and adds it to the client list
 - remove_client : Removes a client from the client list based on the client's name
 - get_client : Returns a client instance based on the client's name
 - get_all_client_balances : Returns a string containing information about all clients and their balances

### Client class 
The Client class represents a bank client.

**Attributes**
 - __id: A unique identifier for the client.
 - name: The name of the client.
 - __balance: The balance of the client's account.
 - transaction_list: A list of transactions associated with the client.

**Methods**
 - __init__ : Initializes a new client with a name and initial balance.
 - __str__ : Returns a string representation of the client.
 - __repr__ : Returns a formal string representation of the client.
 - __eq__ : Checks if two clients are equal based on their name and balance.
 - id : Property to get the client's unique identifier.
 - balance : Property to get the client's balance.
 - balance : Property setter to set the client's balance.
 - depose : Deposits an amount into the client's account.
 - withdraw : Withdraws an amount from the client's account.
 - get_transaction_history : Returns the transaction history of the client.

### Transaction class
Represents a single transaction.

**Attributes:**
 - __id: A unique identifier for the transaction.
 - client_name: The name of the client associated with the transaction.
 - transaction_type: The type of transaction (withdraw or deposit).
 - transaction_amount: The amount of the transaction.
 - transaction_date: The date and time of the transaction.
 - balance_after_operation: The balance of the client's account after the transaction.

**Methods:**
 - __init__ : Initializes a new transaction with the client's name, transaction type, transaction amount, and balance after the operation.
 - id : Property to get the transaction's unique identifier.
 - __str__ : Returns a string representation of the transaction.

### GUI Components: 
##### Features: 
 - add new client
 - show all clients
 - check existing client - view client information, transaction history, perform deposit/withdrawal operations chenging clients balance
 - remove client from the bank