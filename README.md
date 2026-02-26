Expense Tracker (Python CLI Project)
:book: Description
This is a simple Expense Tracker application built using Python.
It allows users to record income and expenses, store them in a JSON file, and calculate the total balance.
The project is designed to practice core Python concepts such as:
Object-Oriented Programming (OOP)
File handling (read/write JSON)
Exception handling
Modular code structure
Loop and conditional logic
:rocket: Features
:heavy_plus_sign: Add a new transaction (Income / Expense)
:page_facing_up: Show all transactions
:moneybag: Calculate current balance
:floppy_disk: Save data persistently using JSON
:warning: Handle invalid inputs safely
🏗 Project Structure
Copy code

expense_tracker/
│
├── main.py
├── transaction.py
├── data_manager.py
└── transactions.json
:small_blue_diamond: transaction.py
Contains the Transaction class that defines the structure of each transaction.
:small_blue_diamond: data_manager.py
Handles loading and saving data from/to the JSON file.
:small_blue_diamond: main.py
Controls the main program flow and user interaction.
🧠 How It Works
The user adds a transaction.
A Transaction object is created.
The object is converted into a dictionary.
The data is saved into transactions.json.
The balance is calculated by:
Adding all incomes
Subtracting all expenses
:arrow_forward: How to Run
Make sure Python is installed, then run:
Copy code

python main.py
:books: What I Learned
Designing a program using multiple modules
Converting objects to dictionaries for JSON storage
Handling user input errors using try/except
Implementing financial logic
Writing cleaner and more maintainable code
:pushpin: Future Improvements
Add delete/edit transaction feature
Add categories (Food, Travel, etc.)
Add monthly reports
Create a GUI version
Add data validation improvements
:man::computer: Author
Developed as a learning project to strengthen backend and Python fundamentals.
