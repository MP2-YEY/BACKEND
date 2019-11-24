#ALGORITHM

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

    print('total expense: ', total_expense)

    print('remaining balance: ', total_income - total_expense)
