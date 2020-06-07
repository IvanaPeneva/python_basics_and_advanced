data=input().split()
wizard_dict={}
while not data[0]=="fight":
    command=data[0]
    name=data[1]
    health=int(data[2])
    damage=int(data[3])
    if command=="new":
        if name not in wizard_dict.keys():
            wizard_dict[name]=[health, damage]
        else:
            print("Wizard already exists!")
    elif command=="edit":
        if name in wizard_dict.keys():
            #wizard_dict[name]=[health, damage]
            current=wizard_dict[name].copy()
            current[0]+=health
            current[1]+=damage
            wizard_dict[name]=current.copy()
        else:
            print("Wizard does not exist!")
    data = input().split()


inp=input().split(" <=> ")
while not inp[0]=="end":
    attaker=inp[0]
    attaked=inp[1]
    if attaker in wizard_dict.keys() and attaked in wizard_dict.keys():
        wizard_dict[attaked][0]-=wizard_dict[attaker][1]
        wizard_dict[attaker][0]+=50

        if wizard_dict[attaked][0]<=0:
            print(f"Fatality - {attaker} wins!")
            wizard_dict.pop(attaked)
        else:
            print(f"Next time {attaked}!")
            #wizard_dict[attaked][0]=attaked_health
    else:
        print("Cannot place a fight with non-existing wizards!")

    inp = input().split(" <=> ")


for name, h_d in sorted(wizard_dict.items(), key=lambda kvp:-kvp[1][0]): #ot h_d health
    print(f"Wizard: {name}. Health: {h_d[0]}. Damage power: {h_d[1]}")

#sor=sorted(wizard_dict.keys(), key=lambda x: wizard_dict[x][0], reverse=True)
#for w in sor:
    #print(f"Wizard: {w}. Health: {wizard_dict[w][0]}. Damage power: {wizard_dict[w][1]}")



