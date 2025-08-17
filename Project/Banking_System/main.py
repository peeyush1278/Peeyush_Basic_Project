import random
n=[]
a = []
p = []
E=[]
b=[]
class sender_details:
    def __init__(self, name,balance,phone,Email):
        self.name = name
        self.balance = balance
        self.phone = phone
        self.Email = Email
        n.append(name)
        account_number=random.randint(1000000000,9999999999)
        while True:
            if account_number in a:
                account_number=random.randint(1000000000,9999999999)
            else:
                a.append(str(account_number))
                break
        p.append(phone)
        E.append(Email)
        b.append(balance)

    def display(self):
        print(f"Name: {n}")
        print(f"Account Number: {a}")
        print(f"Balance: {b}")
        print(f"Phone: {p}")
        print(f"Email: {E}")

while True:
    print("Welcome To Peeyush Bank. How May I Assist You?")
    User_Input = input("Are you New User or Sign In or Exit or Want to Deactivate the account : ")
    if User_Input.lower() == "exit":
        break
    elif User_Input.lower() == "new user":
        print("Please enter your details to create a new account.")
        name = input("Enter your name: ")
        balance = float(input("Enter your balance: "))
        phone = input("Enter your phone number: ")
        Email = input("Enter your email address: ")    
        User=sender_details(name,balance,phone,Email)
        print("Account created successfully!")
        print("Account details are: ")
        User.display()

    elif User_Input.lower() == "sign in":
        print("Please enter your account details to sign in.")
        name= input("Enter your name: ")
        if name in n:
            name_index= n.index(name)
            account = input("Enter your account number: ")
            if account in a:
                account_index = a.index(account)
                if account_index == name_index:
                    phone = input("Enter your phone number: ")
                    if phone in p:
                        phone_index = p.index(phone)
                        if phone_index == name_index:
                            print("Account found!")
                            print("Your account details are: ")
                            print(f"name : {n[name_index]}")
                            print(f"account number : {a[account_index]}")
                            print(f"balance : {b[name_index]}")
                            print(f"phone number : {p[phone_index]}")
                            print(f"email : {E[name_index]}")
                            print(f"Welcome {n[name_index]} thank you for choosing Peeyush bank")
                            while True:
                                print("Welcome To Peeyush Bank. How May I Assist You?(please type exit to exit the system)")
                                User_Input = input()
                                if User_Input.lower() == "exit":
                                    break
                                elif User_Input.lower() == "check balance":
                                    print(f"Your current balance is: {b[name_index]}")
                                elif User_Input.lower() == "deposit":
                                    while True:
                                        amount = float(input("Enter the amount you want to deposit: "))
                                        if amount < 0:
                                            print("invalid number!")
                                        else:
                                            b[name_index] += amount
                                            break
                                elif User_Input.lower() == "withdraw":
                                    while True:
                                        amount = float(input("Enter the amount you want to withdraw: "))
                                        if amount > b[name_index]:
                                            print("Insufficient balance!")
                                        elif amount < 0:
                                            print("invalid number!")
                                        else:
                                            b[name_index] -= amount
                                            break
                                else:
                                    print("invalid operation!")
                        else:
                            print("Incorrect!")
                    else:
                        print("Phone number dosen't exist!")
                else:
                    print("incorrect phone number")
            else:
                print("Account number is not correct!")
        else:
            print("Name not found. Please create a new account.")
    elif User_Input.lower() == "deactivate account":
        print("Please enter your account details to sign in.")
        name= input("Enter your name: ")
        if name in n:
            name_index= n.index(name)
            account = input("Enter your account number: ")
            if account in a:
                account_index = a.index(account)
                if account_index == name_index:
                    phone = input("Enter your phone number: ")
                    if phone in p:
                        phone_index = p.index(phone)
                        if phone_index == name_index:
                            print("Account found!")
                            print("Your account details are: ")
                            print(f"name : {n[name_index]}")
                            print(f"account number : {a[account_index]}")
                            print(f"balance : {b[name_index]}")
                            print(f"phone number : {p[phone_index]}")
                            print(f"email : {E[name_index]}")
                            print(f"Thank you for choosing ZPeeyush bank it was pleasure to have you as our customer! {n[name_index]}")
                            print("Account deactivated!")
                            del n[name_index]
                            del a[account_index]
                            del b[name_index]
                            del E[name_index]
                            del p[phone_index]
                        else:
                                print("invalid operation!")
                    else:
                        print("Phone number dosen't exist!")
                else:
                    print("incorrect phone number")
            else:
                print("Account number is not correct!")
        else:
            print("Name not found. Please create a new account.")
    else:
        print("incorrect inpur please recheck!")


        
        