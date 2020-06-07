class Country:
    def __init__(self, name, persent):
        self.name = name
        self.persent = int(persent)
        self.quar=False

country_list=[]
n =int(input())
for day in range(n):
    inp=input().split()
    command=inp[0]
    country=inp[1]
    acc=Country(name, persent, quar)



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
def main():
    contry_list = []
    n = int(input())
    for day in range(n):
    inp=input().split()
    command=inp[0]
    country=inp[1]

    while data != 'fight':
        wizard_names = list(map(lambda w: w.name, wizards))  # name dict
        command, name, health, damage = data.split()
        if command == 'new':
            if name not in wizard_names:
                obj = Wizard(name, health, damage)
                wizards.append(obj)
            else:
                print("Wizard already exists!")
        elif command == 'edit':
            if name not in wizard_names:
                print("Wizard does not exist!")
            else:
                current_wizard = list(filter(lambda w: w.name == name, wizards))[0]
                current_wizard.health += int(health)
                current_wizard.damage += int(damage)

        data = input()

    battle(wizards)
    for wizard in sorted(wizards, key=lambda w: -w.health):
        print(f"Wizard: {wizard.name}. Health: {wizard.health}. Damage power: {wizard.damage}")


def battle(wizards):
    data = input()
    while data != 'end':
        w1, w2 = data.split(' <=> ')
        wizard_names = list(map(lambda w: w.name, wizards))
        if w1 in wizard_names and w2 in wizard_names:
            attacker = list(filter(lambda w: w.name == w1, wizards))[0]
            attacked = list(filter(lambda w: w.name == w2, wizards))[0]
            attacked.health -= int(attacker.damage)
            attacker.health += 50
            if attacked.health <= 0:
                print(f"Fatality - {attacker.name} wins!")
                wizards.remove(attacked)
            else:
                print(f"Next time {attacked.name}!")
        else:
            print("Cannot place a fight with non-existing wizards!")
        data = input()


if __name__ == '__main__':
    main()






