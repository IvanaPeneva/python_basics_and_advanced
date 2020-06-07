class Country:
    def __init__(self, name, infection, quarantine=False):
        self.name=name
        self.infection=infection
        self.quarantine=quarantine

    def __str__(self):
        return f"{self.name}, {self.infection}"

country_names=input().split(", ")
days=int(input())
country_list=[]

for country in range(len(country_names)): #vajna chast
    obj=Country(str(country_names[country]), 0) #0 za infection
    country_list.append(obj)

for days in range(days):
    command=input().split(" ")

    if command[0]=="Fast_Infect":
        country=str(command[1])
        current_country=list(filter(lambda c: c.name==command[1], country_list)) [0]
        if current_country.quarantine:
            print(f"{current_country} is already under quarantine")
        else:
            current_country.infection+=20

    elif command[0]=="Slow_Infect":
        country=str(command[1])
        current_country=list(filter(lambda c: c.name==command[1], country_list)) [0]
        if current_country.quarantine:
            print(f"{current_country} is already under quarantine")
        else:
            current_country.infection+=10
    elif command[0]=="Cure":
        current_country = list(filter(lambda c: c.name == command[1], country_list))[0]
        current_country.infection=0
    elif command[0]=="Quarantine":
        current_country = list(filter(lambda c: c.name == command[1], country_list))[0]
        if current_country.quarantine:
            print(f"{current_country} is already under quarantine")
        else:
            current_country.quarantine=True
for c in sorted(country_list, key=lambda c:(-c.infection)):
    print(f"{c.name} - {c.infection}% infected")