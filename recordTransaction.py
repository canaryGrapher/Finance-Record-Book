import chalk
import os
import json


def writeToJsonFile(data):
    with open("transactions.json", "r+") as jsonFile:
        file_data = json.load(jsonFile)
        file_data["transactions"].append(data)
        jsonFile.seek(0)
        json.dump(file_data, jsonFile, indent=4, sort_keys=True, default=str)


def recordTransactions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(chalk.blue(
        "Make a selection:\n 1. Record a single transaction\n 2. Record multiple transactions\n 3. Exit"))
    optionSelect = int(input(chalk.yellow("Select an option: ")))
    if optionSelect == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        recordSingleTransaction()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(chalk.green("Last transaction was recorded successfully!\n\n"))
    elif optionSelect == 2:
        recordMultipleTransactions()
    else:
        exit()


def recordSingleTransaction():
    print(chalk.blue("Start entering the transaction details:"))
    description = input(chalk.yellow("Enter the description: "))
    amount = float(input(chalk.yellow("Enter the amount: ")))
    date = input(chalk.yellow("Enter the date (DD/MM/YYYY): "))
    writeToJsonFile({"description": description,
                    "amount": amount, "date": date})
    print(chalk.green("Last transaction was recorded successfully!\n\n"))


def recordMultipleTransactions():
    txnCount = 0
    takeInput = True
    while takeInput:
        recordSingleTransaction()
        anotherInput = input("Add another transaction? (y/n): ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if anotherInput.upper() == "N":
            takeInput = False
            os.system('cls' if os.name == 'nt' else 'clear')
