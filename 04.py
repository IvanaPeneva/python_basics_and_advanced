data=list(map(float,input().split(" ")))
occ_dict={num:data.count(num) for num in data} #vajno
print(occ_dict)
for key,value in sorted(occ_dict.items()):  #sortira po key
    print(f"{key}->{value}")
print()
for key,value in sorted(occ_dict.items(), key=lambda kvp:kvp[1]):  #sortira po value
    print(f"{key}->{value}")
print()
for key,value in sorted(occ_dict.items(), key=lambda kvp:kvp[1], reverse=True):  #sortira po value descending
    print(f"{key}->{value}")
print()
for key,value in sorted(occ_dict.items(), key=lambda kvp:kvp[0], reverse=True):  #sortira po key descending
    print(f"{key}->{value}")
for account in sorted(banking_list, key=lambda acc: (-acc.balance, len(acc.bank))): #sortirane po 2 parametura
    print(f"{account.name} -> {account.balance:.2f} -> ({account.bank})")

for neighborhood, _ in sorted(apartments.items(),key=lambda kvp:kvp[0]): #samo 1vi item shtoto e dict v dict
    print(f"Neighborhood: {neighborhood}")

for segment in sorted(segment_list,key=lambda s: s.distance): #printira samo nai malkoto
    print(segment.show_info())
    break
dogs_list=filter(lambda x :x isinstance(x, Dog),animals_list)

@property
    def age(self):
        return self.__age
@age.setter
    def age(self, value):
        if value < 0:
            print("Age must be positive")
            exit(0)
        else:
            self.__age=value