# DeskBankApp Sample ReadMe

**UTS – Fundamentals of Software Development**
**Lab Project – Group 7**

## 👥 Group Members

| Member   | Student ID |
| -------- | ---------- |
| Akash Nagarkar | Student ID |
| Member 2 | Student ID |
| Member 3 | Student ID |
| Member 4 | Student ID |

> Replace the placeholders above with the names and student IDs of the four group members.

---

## 📌 Project Overview

**DeskBankApp** is a banking application developed as part of the **Fundamentals of Software Development** lab project at the **University of Technology Sydney (UTS)**.

The project demonstrates fundamental software development and object-oriented programming concepts by modelling a simplified banking system. The application represents different banking entities, their attributes, behaviours, and relationships.

The system includes components such as customers, employees, managers, bank accounts, transactions, cards, and branches.

---

## 🎯 Project Objectives

The main objectives of DeskBankApp are to:

* Apply object-oriented programming principles.
* Implement a multi-class software system using Python.
* Represent real-world banking entities as classes and objects.
* Demonstrate relationships between different classes.
* Separate the application into individual Python modules.
* Practise software development concepts covered in the UTS Fundamentals of Software Development subject.
* Develop a maintainable and organised codebase using Git/GitHub.

---

## 🏦 System Components

The application is structured into separate Python files, with each major entity represented by its own class.

```text
DeskBankApp/
│
├── bank.py
├── customer.py
├── manager.py
├── employee.py
├── system_account.py
├── bank_account.py
├── transaction.py
├── cards.py
├── branch.py
│
├── main.py
└── README.md
```

### Main Classes

| Class           | Responsibility                                                   |
| --------------- | ---------------------------------------------------------------- |
| `Bank`          | Central class responsible for coordinating the banking system    |
| `Customer`      | Represents a bank customer                                       |
| `Manager`       | Represents a bank manager and customer-management operations     |
| `Employee`      | Represents a bank employee                                       |
| `SystemAccount` | Handles system account information and login/logout              |
| `BankAccount`   | Represents a customer's bank account and balance                 |
| `Transaction`   | Represents banking transactions such as deposits and withdrawals |
| `Cards`         | Represents bank cards                                            |
| `Branch`        | Represents a bank branch                                         |

---

## 🔗 Class Relationships

The application uses relationships between classes to model how a banking system operates.

For example:

```text
                    ┌─────────────┐
                    │    Bank     │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   Customer            Employee           Manager
        │
        │
        ▼
  BankAccount
        │
        ▼
   Transaction
        │
        ▼
     Cards

        Bank
         │
         ▼
      Branch
```

The `Bank` class acts as the central point for connecting and managing the different objects in the system.

---

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Git
* GitHub
* draw.io / UML
* UTS development environment

---

## ▶️ Running the Application

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd DeskBankApp
```

### 3. Run the application

```bash
python main.py
```

Depending on the Python installation, you may need to use:

```bash
python3 main.py
```

---

## 📂 Project Structure

Each major class is stored in a separate Python file to keep the application modular and easier to maintain.

For example:

```python
from customer import Customer
from bank_account import BankAccount
```

The `bank.py` file acts as the central bank class and maintains connections to the other components rather than duplicating their functionality.

---

## 👨‍💻 Group 7 Development Approach

The project is developed collaboratively by **Group 7**, consisting of four members.

Each member can work on separate classes/modules while following the agreed UML design and coding structure.

### Suggested workflow

1. Create or update the UML design.
2. Assign classes/features to group members.
3. Implement each class in its own Python file.
4. Test individual classes.
5. Integrate the classes through `bank.py` and `main.py`.
6. Test the integrated application.
7. Commit changes to Git.
8. Review and merge changes into the main branch.

---

## 🌿 Git Workflow

The recommended workflow is:

```text
main
 │
 ├── feature/customer
 │
 ├── feature/bank-account
 │
 ├── feature/transaction
 │
 └── feature/branch
```

Group members should create separate branches for their work and merge completed, tested features into the main project.

### Commit example

```bash
git add .
git commit -m "Implement BankAccount class"
git push
```

---

## 🧪 Testing

Each class should be tested independently before integration.

Testing should verify functionality such as:

* Creating customers.
* Creating bank accounts.
* Viewing account balances.
* Depositing funds.
* Withdrawing funds.
* Recording transactions.
* Managing customers.
* Managing employees and managers.
* Managing bank cards.
* Managing branches.
* Connecting objects through the `Bank` class.

---

## 📋 UML Design

The application follows the group's UML design, which defines the principal entities, attributes, methods, and relationships for the banking system.

The UML includes classes such as `Customer`, `Manager`, `Employee`, `Transaction`, `System Account`, `Cards`, `Bank Account`, and `Branch`.

---

## 📚 Academic Context

**University:** University of Technology Sydney (UTS)
**Subject:** Fundamentals of Software Development
**Project:** DeskBankApp
**Group:** Group 7
**Group Size:** 4 members

This project is developed for educational purposes as part of the subject's laboratory/project activities.

---

## 👥 Group 7

**Team:** Group 7
**Members:** 4

> Add the final member names and student IDs before submitting the project.

---

## 📄 License

This project is an academic project developed for the **UTS Fundamentals of Software Development** subject.
