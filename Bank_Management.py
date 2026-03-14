import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data_bank.json'
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fr:
                data = json.load(fr)
        else:
            print("DATABASE FILE NOT FOUND!!!")
    except Exception as error:
        print(f"AN ERROR OCCURRED AS {error}")

    @staticmethod
    def __update_database():
        try:
            with open(Bank.database, 'w') as fs:
                json.dump(Bank.data, fs, indent=4)
        except Exception as error:
            print(f"AN ERROR OCCURRED AS {error}")
    @classmethod
    def __Generate_account_number(cls):
        alphabets = random.choices(string.ascii_letters.upper(), k = 2)
        numbers = random.choices(string.digits, k = 6)
        id = alphabets + numbers
        random.shuffle(id)
        return "".join(id)
    def create_account(self):
        try:
            info = {
                "name": input("Enter your name: "),
                "age": int(input("Enter your age: ")),
                "email": input("Enter your email: "),
                "pin": int(input("Enter your 4 digit pin: ")),
                "Phone_Number" : int(input("Enter your Contanct number: ")),
                "account_number": Bank.__Generate_account_number(),
                "balance": 0,
            }
            if not (info['email'].count('@') == 1 and info['email'].count('.') == 1):
                print("INVALID EMAIL ADDRESS")
                return
            if info['age'] < 18 or len(str(info['pin'])) != 4 or len(str(info['Phone_Number'])) != 10:
                print("SORRY, YOU ARE NOT ELIGIBLE TO OPEN AN ACCOUNT")
                return

            else:
                print("CONGRATS, YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY")

                for i in info:
                    print(f"{i} : {info[i]}")

                print("PLEASE NOTE YOUR ACCOUNT NUMBER FOR FUTURE REFERENCE")

                Bank.data.append(info)
                Bank.__update_database()

        except Exception as error:
            print(f"AN ERROR OCCURRED AS {error}")

    def User_deposit_money(self):
        try:
            user_account_number = input("Enter your account number: ")
            user_pin  = int(input("Enter your 4 digit pin: "))
            found = False
            for i in Bank.data:
                if i['account_number'] == user_account_number and i['pin'] == user_pin:
                    user_deposits_balance = float(input("Enter the amount you want to deposit: "))
                    if user_deposits_balance < 10000000 and user_deposits_balance > 0:
                        i['balance'] += user_deposits_balance
                        print(f"\nName of Account Holder: {i['name']}\nAccount Number of Holder: {i['account_number']}\nBalance in Holder's Account: {i['balance']}\n")
                        Bank.__update_database()
                    
                    else:
                        print(f"SORRY, YOU CAN'T DEPOSIT THIS AMOUNT {user_deposits_balance} IN THE BANK")
                    found = True
                    break
            if found == False:
                print("INVALID ACCOUNT NUMBER OR PIN")
        except Exception as error:
            print(f"AN ERROR OCCURRED AS {error}")  

    def User_withdraw_money(self):
        try:
            user_account_number = input("Enter your account number: ")
            user_pin = int(input("Enter the pin of the account: "))
            found = False
            for i in Bank.data:
                if i['account_number'] == user_account_number and i['pin'] == user_pin:
                    user_withdraw_money = float(input("Enter the amount you want to withdraw: "))
                    if user_withdraw_money <= i['balance'] and user_withdraw_money > 0:
                        i['balance'] -= user_withdraw_money
                        print(f"\nName of Account Holder: {i['name']}\nAccount Number of Holder: {i['account_number']}\nBalance in Holder's Account: {i['balance']}\n")
                        Bank.__update_database()
                    else:
                        print(f"SORRY, YOU CAN'T WITHDRAW THIS AMOUNT {user_withdraw_money} FROM THE BANK")
                    found = True
                    break
            if found == False:
                print("INVALID ACCOUNT NUMBER OR PIN")
        
        except Exception as error:
            print(f"AN ERROR OCCURRED AS {error}")

    def account_details(self):
        try:
            user_account_number = input("Enter your account number: ")
            user_pin = int(input("Enter the pin of the account: "))
            found = False
            for i in Bank.data:
                if i['account_number'] == user_account_number and i['pin'] == user_pin:
                    for keys, items in i.items():
                        print(f"{keys} : {items}")
                    found = True
                    break
            if found == False:
                print("INVALID ACCOUNT NUMBER OR PIN")
        except Exception as error:
            print(f"AN ERROR OCCURRED AS {error}")

    def Update_user_saved_info(self):
        user_account_number = input("Enter your account number: ")
        user_pin = int(input("Enter your pin: "))
        found = False
        for i in Bank.data: 
            if i['account_number'] == user_account_number and i['pin'] == user_pin:
                found = True
                for keys,items in i.items():
                    print(f"{'-' * 40}")
                    print(f"{keys} : {items}")
                print(f"{'-' * 40}")
                print(f"Press 1 to edit the Name: ")
                print(f"Press 2 to edit the Age: ")
                print(f"Press 3 to edit the E-mail: ")
                print(f"Press 4 to edit the Pin: ")
                print(f"Press 5 to edit the Phone Number: ")
                User_choice = int(input("Enter your choice"))
                if User_choice == 1:
                    New_name = input("Enter the new name: ")
                    i['name'] = New_name
                elif User_choice == 2:
                    New_age = int(input("Enter the new age: "))
                    i['age'] = New_age
                elif User_choice == 3: 
                    New_email = input("Enter the new email address: ")
                    i['email'] = New_email
                elif User_choice == 4:
                    New_pin = int(input("Enter your new pin: "))
                    i['pin'] = New_pin
                elif User_choice == 5:
                    New_phone_number = int(input("Enter your new Phone number: "))
                    if len(str(New_phone_number)) == 10:
                        i['Phone_Number'] = New_phone_number
                    else:
                        print("Contact number should be of 10 digits")
                Bank.__update_database()
                break
        if found == False:
            print("INCORRECT PIN OR ACCOUNT NUMBER")
    def User_delete_created_account(self):
        User_account_number = input("Enter your Account number: ")
        User_pin = int(input("Enter your pin: "))
        found = False
        for i in Bank.data:
            if i['account_number'] == User_account_number and i['pin'] == User_pin:
                found = True
                confirmation = input("Do you want to delete your accoount(yes/no): ")
                if confirmation.lower() == 'yes':
                    Bank.data.remove(i)
                    Bank.__update_database()
                    print("ACCOUNT SUCCESSFULLY DELETED")
                    break
                elif confirmation.lower() == 'no':
                    break
                else:
                    print("INCORRECT CHOICE")
                    
        if found == False:
            print("INCORRECT PIN OR ACCOUNT NUMBER")
                    


bank = Bank()

while True:
    print(f"{'-'*40}")
    print("\nPress 1 for creating a new account")
    print("Press 2 for depositing the money in the bank")
    print("Press 3 for withdrawing the money ")
    print("Press 4 for details of the account")
    print("Press 5 for updating the details")
    print("Press 6 for deleting your account")
    print("Press 7 for exiting the program")

    try:
        choice = int(input("Enter your response: "))

        if choice == 1:
            bank.create_account()

        elif choice == 2:
            bank.User_deposit_money()

        elif choice == 3:
            bank.User_withdraw_money()

        elif choice == 4:
            bank.account_details()

        elif choice == 5:
            bank.Update_user_saved_info()

        elif choice == 6:
            bank.User_delete_created_account()

        elif choice == 7:
            print("THANK YOU FOR USING OUR SERVICES")
            break

        else:
            print("INVALID CHOICE")

    except Exception as error:
        print(f"AN ERROR OCCURRED AS {error}")