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
              f"{self.cc_number}\nCC Type: {self.cc_type}\nBalance: {self.balance}\nAccount NO: {self.account_no}")
        print("-------------------------")
        print()


# Methods/Functions...

def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def findUser():
    first_name_list = []
    user_first_name = input("Enter user's first name: ").title()
    print()
    name_values_found = 0
    for user in userList:
        if user_first_name == user.first_name:
            first_name_list.append(user)
            name_values_found += 1
    if name_values_found == 0:
        print("There are no users with that name.")
        return
    print(f"Here are the users with the first name {user_first_name}:")
    for user in first_name_list:
        print(user.first_name, user.last_name)
    print()
    user_last_name = input("Enter user's last name: ").title()
    print()
    found = False
    for user in first_name_list:
        if user_last_name == user.last_name:
            User.displayInfo(user)
            found = True
    if not found:
        print("There is no user with that name.")
        return


def overdrafts():
    # TO COMPLETE
    True


def missingEmails():
    # TO COMPLETE
    True


def bankDetails():
    # TO COMPLET
    True


def transfer():
    # TO COMPLETE
    True


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
    userChoice = input("Enter choice: ")
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
