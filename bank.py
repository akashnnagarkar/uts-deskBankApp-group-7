# bank.py

from customer import Customer
from manager import Manager
from employee import Employee
from transaction import Transaction
from system_account import SystemAccount
from cards import Cards
from bank_account import BankAccount
from branch import Branch


class Bank:
    def __init__(self, name):
        self.name = name

        self.customers = []
        self.managers = []
        self.employees = []
        self.accounts = []
        self.transactions = []
        self.system_accounts = []
        self.cards = []
        self.branches = []

    # -------------------------
    # Customer
    # -------------------------

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer_id):
        self.customers = [
            customer for customer in self.customers
            if customer.customerId != customer_id
        ]

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customerId == customer_id:
                return customer
        return None

    # -------------------------
    # Manager
    # -------------------------

    def add_manager(self, manager):
        self.managers.append(manager)

    # -------------------------
    # Employee
    # -------------------------

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.employeeId == employee_id:
                return employee
        return None

    # -------------------------
    # Bank Account
    # -------------------------

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.number == account_number:
                return account
        return None

    # -------------------------
    # Transaction
    # -------------------------

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    # -------------------------
    # System Account
    # -------------------------

    def add_system_account(self, account):
        self.system_accounts.append(account)

    # -------------------------
    # Cards
    # -------------------------

    def add_card(self, card):
        self.cards.append(card)

    # -------------------------
    # Branch
    # -------------------------

    def add_branch(self, branch):
        self.branches.append(branch)

    def find_branch(self, branch_id):
        for branch in self.branches:
            if branch.branchId == branch_id:
                return branch
        return None