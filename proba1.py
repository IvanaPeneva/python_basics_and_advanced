man=input()
if man.isalpha():
    print(f"{man} is alpha man")
else:
    print(f"{man} is not a alpha man")
country_list=input().split(", ")
n=int(input())
infection_dict={}
for day in range(n):
    inp=input().split()
    command=inp[0]
    country=inp[1]
    infection_dict[country]={"persent":0, "quar":False}
    if country in country_list:
        if command=="Fast_Infect" and infection_dict[country]["quar"]==False:
            infection_dict[country]["persent"]+=20
        if command=="Slow_Infect" and infection_dict[country]["quar"]==False:
            infection_dict[country]["persent"]+=10
        if command=="Quarantine" and infection_dict[country]["quar"]==False:
            infection_dict[country]["quar"] =True
        if command == "Quarantine" and infection_dict[country]["quar"] == True:
            print(f"{country} is already under quarantine")
        if command=="Cure":
            infection_dict[country]["persent"]=0
#for _, a in infection_dict.items():
    #for persent, quar in infection_dict[country].items():
        #print(f"{persent} - {quar}")
for country, _ in infection_dict.items():
    for kvp in infection_dict[country].items():
        print(f"{kvp}")
