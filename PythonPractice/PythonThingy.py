import math

def unoReverse(x):
    return x[::-1]

def findMaxIndex(x):
    return x.index(max(x))

def odds(x):
    return [odd for odd in x if odd % 2 != 0]

def euclidianDistance(coor1, coor2):
    return math.sqrt(sum([(x-y)**2 for x, y in zip(coor1, coor2)]))

def fileLineFinder(file):
    lines = []

    with open(file, 'r') as filehandler:
        contents = filehandler.readlines()

        for line in contents:
            indexPostions = line[:-1]
            lines.append(indexPostions)

        return print(lines)

def fileWriter(file, list):
    with open(file, 'w') as filehandler:
        for listItems in list:
            filehandler.write('%s\n' % listItems)

        return filehandler


class BankAccount:
    ID = ""
    deposit = 0
    balance = 0
    withdraw = 0

    def __init__(self, name, current_balance):
        self.ID = name
        self.balance = current_balance
        self.deposit = 0
        self.withdraw = 0

    def deposit_money(self, money):
        self.deposit = money
        self.balance = self.deposit + self.balance
        print("Your current balance is: ")
        print(self.balance)
        return self.balance

    def withdraw_money(self, money):
        self.withdraw = money
        self.balance = self.balance - self.withdraw
        print("Your current balance is: ")
        print(self.balance)
        return self.balance


obj_1 = BankAccount("Cameron", 1000)
obj_2 = BankAccount("Dave", 500)

obj_1.withdraw_money(500)
obj_2.deposit_money(500)