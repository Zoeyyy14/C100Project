class Atm(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def checkBalance(self):
        Card_number = input("Enter Your Card Number")
        Pin_number = input("Enter The Pin Number")
        print("Your Balnace Is 5000000000 dollars")
    def withdraw(self):
        Card_number = input("Enter Your Card Number")
        Pin_number = input("Enter The Pin Number")
        print("I Want To Withdraw 1 dollar")
    def remainingBalance(self):
        Card_number = input("Enter Your Card Number")
        Pin_number = input("Enter The Pin Number")
        print("4999999999")

Card1 = Atm(12345, 1234)
print(Card1.checkBalance())
print(Card1.withdraw())
print(Card1.remainingBalance())