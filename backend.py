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
#
#
# NOTE: get one input ng isang object tas ilagay sa dictionary and put sa file
# DIFF CLASS: EXPENSE OR INCOME


class income():
    def __init__(date, types, amount, note):
        self.date = date
        self.type = types
        self.amount = amount
        self.note = note


date = raw_input('Enter date: ')
types = raw_input('Enter types: ')
amount = raw_input('Enter amount: ')
note = raw_input('Enter note: ')

new_object = myStruct(name, salary, dob, title)
