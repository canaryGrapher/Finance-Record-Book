import os
import chalk
import json


def calculateBudget():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print(chalk.blue("Calculate budget:\n 1. Calculate current budget\n 2. Calculate budget for a specific month\n 3. Exit"))
    optionSelect = int(input(chalk.yellow("Select an option: ")))
    if optionSelect == 1:
        calculateCurrentBudget()
        # os.system('cls' if os.name == 'nt' else 'clear')
        calculateBudget()
    elif optionSelect == 2:
        calculateBudgetForMonth()
        os.system('cls' if os.name == 'nt' else 'clear')
        calculateBudget()
    elif optionSelect == 3:
        exit()


def calculateCurrentBudget():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("transactions.json", "r+") as jsonFile:
        file_data = json.load(jsonFile)
        transactions = file_data["transactions"]
        total = 0
        for transaction in transactions:
            total += float(transaction["amount"])
        print(chalk.green("\nCurrent budget: " + str(total) + "\n"))


def calculateBudgetForMonth():
    print(chalk.red("This function is under development!"))
