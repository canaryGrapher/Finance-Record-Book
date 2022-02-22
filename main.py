import os
import chalk

import recordTransaction
import viewTransaction
import budgetCalculations
import exportTransactions


def onLaunch():
    print(chalk.blue(
        "Book keeping program:\n 1. Record new transaction\n 2. Calculate current budget\n 3. View Transactions\n 4. Export transactions\n 5. Exit"))
    optionSelect = int(input(chalk.yellow("Select an option: ")))
    if optionSelect == 1:
        recordTransaction.recordTransactions()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(chalk.green("Last transaction was recorded successfully!\n\n"))
        onLaunch()
    elif optionSelect == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        budgetCalculations.calculateBudget()
        onLaunch()
    elif optionSelect == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        viewTransaction.viewTransactionsMenu()
        onLaunch()
    elif optionSelect == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        exportTransactions.exportList()
        onLaunch()
    else:
        exit()


onLaunch()
