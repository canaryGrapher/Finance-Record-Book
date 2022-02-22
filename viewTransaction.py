from optparse import TitledHelpFormatter
import os
import chalk
import json
from tabulate import tabulate


def viewTransactionsMenu():
    print(chalk.blue(
        "Book keeping program:\n 1. View all transactions\n 2. View last n transactions\n 3. View transactions in date range\n 4. Exit"))
    optionSelect = int(input(chalk.yellow("Select an option: ")))
    if optionSelect == 1:
        viewAllTransactions()
        print("\n\n")
        viewTransactionsMenu()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif optionSelect == 2:
        viewLastNTransactions()
        print("\n\n")
        viewTransactionsMenu()
        os.system('cls' if os.name == 'nt' else 'clear')
        viewTransactionsMenu()
    elif optionSelect == 3:
        viewTransactionsInDateRange()
        print("\n\n")
        viewTransactionsMenu()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif optionSelect == 4:
        exit()


def viewAllTransactions():
    os.system('cls' if os.name == 'nt' else 'clear')
    budget = []
    budget.append(['Date', 'Amount', 'Description'])
    with open("transactions.json", "r+") as jsonFile:
        file_data = json.load(jsonFile)
        transactions = file_data["transactions"]
        for transaction in transactions:
            date = transaction["date"]
            amount = transaction["amount"]
            description = transaction["description"]
            budget.append([date, amount, description])
    print(tabulate(budget, headers='firstrow',
          showindex="always", tablefmt="grid"))


def viewLastNTransactions():
    os.system('cls' if os.name == 'nt' else 'clear')
    # take input of how many transactions to view
    numberOfTransactions = int(
        input(chalk.yellow("Enter the number of transactions to view: ")))
    budget = []
    budget.append(['Date', 'Amount', 'Description'])
    with open("transactions.json", "r+") as jsonFile:
        file_data = json.load(jsonFile)
        transactions = file_data["transactions"]
        totalDisplay = 0
        for transaction in transactions:
            if totalDisplay < numberOfTransactions:
                totalDisplay += 1
                date = transaction["date"]
                amount = transaction["amount"]
                description = transaction["description"]
                budget.append([date, amount, description])
    print(tabulate(budget, headers='firstrow',
          showindex="always", tablefmt="grid"))


def viewTransactionsInDateRange():
    os.system('cls' if os.name == 'nt' else 'clear')
    # take input of intial date
    initialDate = str(
        input(chalk.yellow("Enter the initial date in DD/MM/YYYY format: ")))
    # take input of final date
    finalDate = str(
        input(chalk.yellow("Enter the final date in DD/MM/YYYY format: ")))
    budget = []
    budget.append(['Date', 'Amount', 'Description'])
    intialDate, intialMonth, intialYear = initialDate.split("/")
    finalDate, finalMonth, finalYear = finalDate.split("/")
    with open("transactions.json", "r+") as jsonFile:
        file_data = json.load(jsonFile)
        transactions = file_data["transactions"]
        for transaction in transactions:
            targetDate, targetMonth, targetYear = transaction["date"].split(
                "/")
            if targetDate <= finalDate and targetDate >= intialDate and targetMonth <= finalMonth and targetMonth >= intialMonth and targetYear <= finalYear and targetYear >= intialYear:
                date = transaction["date"]
                amount = transaction["amount"]
                description = transaction["description"]
                budget.append([date, amount, description])

    print(tabulate(budget, headers='firstrow',
          showindex="always", tablefmt="grid"))
