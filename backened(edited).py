# PLAN:
#   1. USER INPUTS DATA  (TREAT AS AN OBJECT - MAKE DICTIONARY)
#          - CHOICE: INCOME OR EXPENSE
#          - ENTER DATE
#          - CHOOSE EXPENSE TYPE
#          - DISPLAYS CALCULATOR () TO ENTER THE AMOUNT
#          - CHOICE IF HE'LL ENTER NOTE
#          - PARSE IF A BUTTON IS PRESSED
#   2. STORE DATA IN FILE
#           - OBJECT WILL BE STORED IN THE FILE
#   3. ACCESS DATA FROM THE FILE
#           - READ THE FILE TO SEE THE DATA
#   4. DISPLAY THE LIST OF INCOME AND EXPENSES AND THE OTHER DATA PER DAY
#   5. MAKE AN ALGORITHM THAT WILL COMPUTE FOR THE REMAINING BALANCE EVERYTIME THE USER INPUTS INCOME OR EXPENSE (PER DAY/ PER MONTH)
#   6. DISPLAY GRAPH BASED ON STATISTICS OF INCOME AND EXPENSE
#
# NOTE: get one input ng isang object tas ilagay sa dictionary and put sa file
# DIFF CLASS: EXPENSE OR INCOME

# IN THIS PART, YOU WILL SEE THE READING AND WRITING ON A FILE AS WELL AS THE CALCULATOR TO BE USED TO COMPUTE FOR THE TOTAL AMOUNT OF EXPENSE OR INCOME

import re


class Income:
    def __init__(self, date, types, amount, note):
        self.date = date
        self.types = types
        self.amount = amount
        self.note = note


class Expense:
    def __init__(self, date, types, amount, note):
        self.date = date
        self.types = types
        self.amount = amount
        self.note = note


# print("Our Magical Calculator")
# print("Type x to close")
previous = 0
run = True


def performMath():  # this is the code for the calculator source: https://www.includehelp.com/python/design-traditional-and-magic-calculator-in-python3.aspx
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Input Amount to calculate: ")
    else:
        equation = input(str(previous))

    if equation == 'x':
        exit(0)  # terminate the program when x is entered
    else:
        equation = re.sub('[a-zA-Z,:()" "]', "", equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)
    return previous

# WE WILL INTEGRATE HERE THE EXPENSE OR INCOME BUTTON IN THE GUI
choice = input("Do you want to input a transaction?(yes or no): ").lower()
if choice == "yes":
    button = input('(1)Income (2)Expense (press 1 or 2): ').lower()

    if button == "1":
        date = input('Enter date (MM/DD/YYYY): ')
        types = input('Enter type (e.g. salary, allowance, gift, etc.): ')
        # We're now calling the calculator function. It asks the amount to calculate.
        amount = performMath()
        note = input('Enter note: ')
        # We accept this 4 parameters
        new_Income = Income(date, types, amount, note)
        newIncomeList = [new_Income.date, new_Income.types,
                         new_Income.amount, new_Income.note]  # we put it in a list
        # Here we open a file. "a+" means that it's an append type of file. If the file isn't existing, it will create a new one, otherwise, it will allow us to append object to the file
        income = open("IncomeData.txt", "a+")
        # appends the object parameter, it is in list form.
        income.write(str(newIncomeList) + "\n")
        income.close()        
    elif button == "2":  # the notes on the button == income also applies here
        date = input('Enter date(MM/DD/YYYY): ')
        types = input('Enter type (e.g. food, transport, school, etc.): ')
        amount = performMath()
        note = input('Enter note: ')
        new_Expense = Expense(date, types, amount, note)
        newExpenseList = [new_Expense.date, new_Expense.types,
                          new_Expense.amount, new_Expense.note]
        expense = open("ExpenseData.txt", "a+")
        expense.write(str(newExpenseList) + "\n")
        expense.close()

# From here, it will read each line in each Class (expense and income) and sort it in a list based on their date
view = input(
    "Which transaction do you want to view? (expense or income): ").lower()

if view == "income":
    with open('IncomeData.txt', 'r') as income:
        data = []
        for line in income:  # converts each data in the text file in to a readable list
            each_data = line[2:len(line)-3]
            dataList = each_data.split(",")
            data.append(dataList)
        copyData = data.copy()
        # print(copyData)
        sortedDate = []
        for x in copyData:
            if x[0] == True:
                continue
            store = []
            for y in copyData:
                if x[0] == y[0]:
                    store.append(y)
            if store not in sortedDate:
                sortedDate.append(store)
        # displays each transaction according to their dates
        for display in sortedDate:
            print("Date:", display[0][0])
            for x in display:
                print("Type:", x[1], "Amount:",
                      x[2], "Note:", x[3])
            print()
            
elif view == "expense":
    with open('ExpenseData.txt', 'r') as income:
        data = []
        for line in income:  # converts each data in the text file in to a readable list
            each_data = line[2:len(line)-3]
            dataList = each_data.split(",")
            data.append(dataList)
        copyData = data.copy()
        # print(copyData)
        sortedDate = []
        for x in copyData:
            if x[0] == True:
                continue
            store = []
            for y in copyData:
                if x[0] == y[0]:
                    store.append(y)
            if store not in sortedDate:
                sortedDate.append(store)
        # displays each transaction according to their dates
        for display in sortedDate:
            print("Date:", display[0][0])
            for x in display:
                print("Type:", x[1], "Amount:",
                      x[2], "Note:", x[3])
            print()

#ALGORITHM TO COMPUTE FOR THE REMAINING BALANCE

def algo():

    #COMPUTES TOTAL INCOME

    with open('IncomeData.txt', 'r') as income:
        data = []
        for line in income:
            each_data = line[2:len(line)-3]
            dataList = each_data.split(", ")
            data.append(dataList)
        copyData = data.copy()
        sortedDate = []
        for x in copyData:
            if x[0] == True:
                continue
            store = []
            for y in copyData:
                if x[0] == y[0]:
                    store.append(y)
            if store not in sortedDate:
                sortedDate.append(store)
       
    list_income=[int(i[0][2]) for i in sortedDate]

    total_income = sum(list_income)

    print('total income: ', total_income)

    #COMPUTES TOTAL EXPENSE

    with open('ExpenseData.txt', 'r') as expense:
        data = []
        for line in expense:
            each_data = line[2:len(line)-3]
            dataList = each_data.split(", ")
            data.append(dataList)
        copyData = data.copy()
        sortedDate = []
        for x in copyData:
            if x[0] == True:
                continue
            store = []
            for y in copyData:
                if x[0] == y[0]:
                    store.append(y)
            if store not in sortedDate:
                sortedDate.append(store)
       
    list_expense = [int(i[0][2]) for i in sortedDate]

    total_expense = sum(list_expense)

    print('total expenses: ', total_expense)
    print()
    print('remaining balance: ')
    
    return total_income - total_expense
    

choice = input("Would you like to see your remaining balance?(yes or no): ").lower()
if choice == "yes":
    print(algo())