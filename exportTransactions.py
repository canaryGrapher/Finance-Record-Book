from fileinput import filename
import chalk
import os
import time

import json
import csv
from tabulate import tabulate
import xlsxwriter


def exportList():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_data = open("transactions.json", "r+")
    data = json.loads(file_data.read())
    print(chalk.blue(
        "What format do you want to export? :\n 1. JSON\n 2. CSV\n 3. TXT\n 4. XLXS\n 5. Exit\n"))
    optionSelect = int(input(chalk.yellow("Select an option: ")))
    if optionSelect == 1:
        exportAsJSON(data)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(chalk.green("Export as JSON successful!\n\n"))
        exportList()
    elif optionSelect == 2:
        exportAsCSV(data)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif optionSelect == 3:
        exportAsTXT(data)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif optionSelect == 4:
        exportAsXLXS(data)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        exit()


def exportAsJSON(data):
    fileName = "exports/" + str(time.time()) + "_export" + ".json"
    newFile = open(fileName, "w+")
    transactions = data["transactions"]
    json.dump(transactions, newFile, indent=4, sort_keys=True)


def exportAsCSV(data):
    fileName = "exports/" + str(time.time()) + "_export" + ".csv"
    newFile = open(fileName, "w+")
    csv_writer = csv.writer(newFile)
    csv_writer.writerow(["Date", "Amount", "Description"])
    transactions = data["transactions"]
    for transaction in transactions:
        date = transaction["date"]
        amount = transaction["amount"]
        description = transaction["description"]
        csv_writer.writerow([date, amount, description])


def exportAsTXT(data):
    fileName = "exports/" + str(time.time()) + "_export" + ".txt"
    newFile = open(fileName, "w+")
    budget = []
    budget.append(['Date', 'Amount', 'Description'])
    transactions = data["transactions"]
    for transaction in transactions:
        date = transaction["date"]
        amount = transaction["amount"]
        description = transaction["description"]
        budget.append([date, amount, description])
    fileData = tabulate(budget, headers='firstrow',
                        showindex="always", tablefmt="grid")
    newFile.writelines(fileData)


def exportAsXLXS(data):
    fileName = "exports/" + str(time.time()) + "_export" + ".xlxs"
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet("transactions")
    worksheet.write(0, 0, "Date")
    worksheet.write(0, 1, "Amount")
    worksheet.write(0, 2, "Description")
    row = 1
    transactions = data["transactions"]
    for transaction in transactions:
        date = transaction["date"]
        amount = transaction["amount"]
        description = transaction["description"]
        print(date, amount, description)
        worksheet.write(row, 0, date)
        worksheet.write(row, 1, amount)
        worksheet.write(row, 2, description)
        row += 1
    workbook.close()
