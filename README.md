🏧 Python ATM Basic Project
A simple ATM simulation project in Python created to practice basic Python and Object-Oriented Programming (OOP) concepts.

📌 Project Overview
This project simulates a basic ATM system where a user can:

Enter their name

Set a PIN

Set an opening balance

Verify their PIN

Check account balance

Deposit money

Withdraw money

Exit the ATM

The project uses a Python ATM class and methods to handle the different ATM operations.

✨ Features
1. PIN Verification
The user enters a PIN before accessing the ATM menu. If the PIN is incorrect, access is denied.

2. Check Balance
Displays the user's current account balance.

3. Deposit Money
Allows the user to enter a deposit amount. Only amounts greater than 0 are accepted.

4. Withdraw Money
Allows the user to withdraw money if:

The withdrawal amount is greater than 0

The requested amount does not exceed the available balance

5. ATM Menu
The program provides a continuous menu with these options:

===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
🛠️ Concepts Used
This beginner-friendly project demonstrates:

Python classes and objects

__init__() constructor

Instance variables

Methods

if, elif, and else

while loop

User input with input()

Type conversion using float()

String formatting with f-strings

Basic validation

Object-Oriented Programming (OOP)

📂 Project Structure
python-basic-project/
│
├── python_basic_project.py
└── README.md
▶️ How to Run
Step 1: Install Python
Make sure Python is installed on your computer.

Check the installation:

python --version
Step 2: Clone the Repository
git clone <your-repository-url>
Step 3: Open the Project Folder
cd python-basic-project
Step 4: Run the Program
python python_basic_project.py
💻 Example Flow
Enter your name: Shatrughan
Set your PIN: 1234
Enter opening balance: 5000

Enter your PIN: 1234

Welcome, Shatrughan!

===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter choice: 1

Current Balance: 5000.0
🎯 Purpose
This project was created as a Python basic/OOP practice project. It is intended for learning and does not represent a real banking or ATM system.

👨‍💻 Author
Shatrughan Tiwari

📜 License
This project is created for educational and learning purposes.

