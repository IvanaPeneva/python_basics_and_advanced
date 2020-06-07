class BankAccount:
    def __init__(self, name, bank, balance):
        self.name=name
        self.bank=bank
        self.balance=balance
banking_list=[]
data=input().split(" | ")
while not data[0]=="end":
    name=data[1]
    bank=data[0]
    balance=float(data[2])
    account=BankAccount(name=name, bank=bank, balance=balance) #priravnqvane
    banking_list.append(account)
    data = input().split(" | ")
for account in sorted(banking_list, key=lambda acc: (-acc.balance, len(acc.bank))): #sortirane po 2 parametura
    print(f"{account.name} -> {account.balance:.2f} -> ({account.bank})")
