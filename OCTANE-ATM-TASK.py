import time

class ATM:
    atm_name="ABC ATM"
    userinfo=dict()

    def __init__(self,user,pin):
        self.user=user
        self.pin=pin
        self.balance=0.0
        self.transactions=[]
        self.userinfo[self.user]=self.pin

    def login(self):
        self.reuser=input("ENTER USER ID:")
        self.repin=int(input("ENTER PIN:"))
        if self.reuser in self.userinfo and self.userinfo.get(self.reuser) == self.repin:
            print("                                    Login Successful!")
            print(f"                                   WELCOME TO {self.atm_name}")  
            self.choice()

        else:
            print("entered user ID or user PIN is wrong")
            print("          !!try again!!")

    def choice(self):
        while True:
            print(" enter 1 for checking balance")
            print(" enter 2 for deposit")
            print(" enter 3 for with draw")
            print(" enter 4 for transactions history")
            print(" enter 5 for transfer")
            print(" enter 6 for quit")
            print(" enter 7 for users")
            print("enter 8 for change pin")

            cho=input("ENTER YOUR OPERATION:")


            if cho=="1":
                    self.cbalance()
            elif cho=="2":
                self.deposit()
            elif cho=="3":
                self.withdraw()
            elif cho=="4":
                self.transactionh()
            elif cho=="5":
                self.transfer()
            elif cho=="7":
                self.userinf()
            elif cho=="8":
                self.change()
            elif cho=="6":
                print("!!THANK YOU FOR VISITING OUR ATM!!")
                print("        !!VISIT AGAIN!!")
                break
            else:
                print("cannot run this operation")



    def cbalance(self):
        print(f"your balance is {self.balance}")

    def deposit(self):
        bal=float(input("enter the amount to deposit:"))
        self.balance+=bal
        self.transactions.append(f"deposited {bal} at {time.asctime(time.localtime(time.time()))}")
        print(f"{bal} amount has successfully deposited at {time.asctime(time.localtime(time.time()))}")

    def withdraw(self):
        withd=float(input("enter the amount to withdraw:"))
        if withd<=self.balance:
            self.balance-=withd
            print(f"{withd} has been withdrawn successfully at {time.asctime(time.localtime(time.time()))}")
            self.transactions.append(f"withdrawed {withd} at {time.asctime(time.localtime(time.time()))}")
        else:
            print("           !!insufficient balance!!")

    def transactionh(self):
        if len(self.transactions) == 0:
            print("no transaction history")
        else:
            for i in self.transactions:
                print(i)

    def userinf(self):
        for i in self.userinfo:
            print(i)

    def transfer(self):
        self.rname=input("enter the USER ID of receiver:")

        if (self.rname in self.userinfo):
            print("           !!user found!!")
            amt=float(input("enter the amount to send:"))
            if amt <= self.balance:
                self.balance-=amt
                print(f"successfully sent {amt} to {self.rname}")
                self.transactions.append(f"sent {amt} to {self.rname} at {time.asctime(time.localtime(time.time()))}")
            else:
                print("insufficient balance")
        else:
            print(f"no user found with {self.rname} user id")


    def change(self):
        pin1=int(input("enter the pin:"))
        pin2=int(input("enter the new pin:"))
        pin3=int(input("enter the new pin again:"))
        if pin1==self.repin:
            if pin2==pin3:
                self.repin=pin3
                print("PIN changed successfully")
            else:
                print("new pins do not match")
        else:
            print("wrong PIN entered")



        
u1=ATM("tyui",34523)
u2=ATM("qwer",5354)
u3=ATM("abcd",9876)
u4=ATM("zxcv",2345)

u3.login()


