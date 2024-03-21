# Imports...
import math


# Classes...
class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type,
                 balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def displayInfo(self):
        print("***** USER DETAILS: *****")
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nGender: {self.gender}\n"
              f"Street Address: {self.street_address}\nCity: {self.city}\nEmail: {self.email}\nCC Number:"
              f"{self.cc_number}\nCC Type: {self.cc_type}\nBalance: ${self.balance:.2f}\nAccount NO: {self.account_no}")
        print("-------------------------")
        print()


class IntegerException(Exception):
    "Passes if amount is not an integer"
    pass


# Methods/Functions...

def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def findUser():
    first_name_list = []
    print("--- FIND USER ---")
    user_first_name = input("Enter user's first name: ").title()
    name_values_found = 0
    for user in userList:
        if user_first_name == user.first_name:
            first_name_list.append(user)
            name_values_found += 1
    if name_values_found == 0:
        print("There are no users with that name.")
        print("-----------------")
        print()
        return
    print(f"Here are the users with the first name {user_first_name}:")
    for user in first_name_list:
        print(user.first_name, user.last_name)
    print()
    user_last_name = input("Enter user's last name: ").title()
    found = False
    for user in first_name_list:
        if user_last_name == user.last_name:
            print()
            User.displayInfo(user)
            found = True
    if not found:
        print("There is no user with that name.")
        print("-----------------")
        print()
        return


def overdrafts():
    total_users = 0
    print("--- USERS WITH OVERDRAFT ---")
    for user in userList:
        if user.balance < 0:
            total_users += 1
            print(f"{user.first_name} {user.last_name}: ${user.balance:.2f}")
    print(f"Total users with overdraft: {total_users}")
    print("----------------------------")
    print()


def missingEmails():
    total_users = 0
    print("--- USERS WITHOUT EMAILS ---")
    for user in userList:
        if not user.email:
            total_users += 1
            print(f"{user.first_name} {user.last_name}")
    print(f"Total users without an email: {total_users}")
    print(f"---------------------------")
    print()


def bankDetails():
    total_users = 0
    total_balance = 0
    lowest_user = ""
    lowest_balance = 0
    highest_user = []
    highest_balance = 0
    print("--- TOTAL BANK STATEMENT ---")
    for user in userList:
        total_users += 1
        total_balance += user.balance
        if user.balance < lowest_balance:
            lowest_user = f"{user.first_name} {user.last_name}"
            lowest_balance = user.balance
        elif user.balance > highest_balance:
            highest_user = f"{user.first_name} {user.last_name}"
            highest_balance = user.balance
    print(f"Total users in the system: {total_users}")
    print(f"Total bank balance: ${total_balance:.2f}")
    print(f"User with lowest balance: {lowest_user} (${lowest_balance:.2f})")
    print(f"User with highest balance: {highest_user} (${highest_balance:.2f})")
    print(f"---------------------------")
    print()


def int_check(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check,int):
                valid = True
                return number_to_check
        except ValueError:
            print("Value must be an integer.")
            print()


def transfer():
    print("--- BANK TRANSFER ---")
    send = input("Enter bank account number to withdraw from (or 'Q' to quit): ").upper()
    if send == "Q":
        print("---------------------")
        print()
        return
    found_account = False
    for user in userList:
        if send == user.account_no:
            send_account_balance = user.balance
            print(f"Name: {user.first_name} {user.last_name}")
            print(f"Balance: ${user.balance}")
            print()
            found_account = True
    if not found_account:
        print("That is not a valid account number.")
        print()
        return
    valid = False
    while not valid:
        amount = int_check("Enter amount to transfer: ")
        if amount > send_account_balance:
            print("Transfer quantity can not exceed account balance.")
            print()
        else:
            valid = True
    receive = ""
    found_account = False
    print()
    while not found_account:
        receive = input(f"Enter bank account number to deposit ${amount} into (or 'Q' to quit): ").upper()
        if receive == "Q":
            print("---------------------")
            print()
            return
        for user in userList:
            if receive == user.account_no:
                withdraw_account_balance = user.balance
                print(f"Name: {user.first_name} {user.last_name}")
                print(f"Balance: {user.balance}")
                print()
                found_account = True

    confirm = input((f"Press >ENTER< to confirm that you want to transfer ${amount} from account "
                     f"{send} to {receive} (or 'Q' to quit): ")).upper()
    if confirm == "Q":
        print("---------------------")
        print()
        return
    elif confirm == "":
        send.balance -= amount
        receive.balance += amount
        print(f"${amount} has been transferred from {send} to {receive}.")
        print("---------------------")
        print()
        return
    else:
        print("That is not a valid choice. Transfer cancelled.")
        print("---------------------")
        print()
        return


# Main...
userList = []
generateUsers()

userChoice = ""
while userChoice != "Q":
    print(">>> What function would you like to run? <<<")
    print("1: Find User")
    print("2: Print Overdraft Information")
    print("3: Print Users With Missing Emails")
    print("4: Print Bank Details")
    print("5: Transfer Money")
    print("Q: Quit")
    userChoice = input("Enter choice: ").upper()
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()