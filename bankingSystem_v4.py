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
              f"{self.cc_number}\nCC Type: {self.cc_type}\nBalance: {self.balance:.2f}\nAccount NO: {self.account_no}")
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
            print(f"{user.first_name} {user.last_name}: {user.balance:.2f}")
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
    print(f"Total bank balance: {total_balance:.2f}")
    print(f"User with lowest balance: {lowest_user} ({lowest_balance:.2f})")
    print(f"User with highest balance: {highest_user} ({highest_balance:.2f})")
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


def transfer():
    withdraw_account = input("Enter the account number you want to transfer "
                             "money FROM: ")
    for user in userList:
        if user.account_no == withdraw_account:
            withdraw_user = user
            print(f"\nUser is: {withdraw_user.first_name} "
                  f"{withdraw_user.last_name}\n"
                  f"Account No:{withdraw_user.account_no}\nBalance $"
                  f"{withdraw_user.balance}")
    transfer_amount = int_check("\nHow much do you want to transfer? $")
    deposit_account = input("\nEnter the account number you want to transfer "
                            "money TO: ")
    for user in userList:
        if user.account_no == deposit_account:
            deposit_user = user
            confirm = input(f"\nDo you want to transfer ${transfer_amount}\n"
                            f"to {deposit_user.first_name} "
                            f"{deposit_user.last_name}\nwith a "
                            f"current balance of ${deposit_user.balance}\n"
                            f"\nPress <enter> to confirm OR any other key and "
                            f"<enter> to return to the main menu\n")
            if not confirm:
                withdraw_user.balance -= transfer_amount
                deposit_user.balance += transfer_amount
                print(f"${transfer_amount} has just been transferred\n"
                      f"from {withdraw_user.first_name} "
                      f"{withdraw_user.last_name} leaving a new balance of $"
                      f"{withdraw_user.balance}\n"
                      f"to {deposit_user.first_name} {deposit_user.last_name} "
                      f"leaving a new balance of ${deposit_user.balance}")
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
