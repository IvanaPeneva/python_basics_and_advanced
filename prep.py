country_list=input().split(", ")
n=int(input())
infection_dict={}
counter=0
for day in range(n):
    inp=input().split()
    command=inp[0]
    country=inp[1]
    infection_dict[country]={"persent":0}
    if country in country_list:
        if command=="Fast_Infect":
            infection_dict[country]["persent"]+=20
        if command=="Slow_Infect":
            infection_dict[country]["persent"]+=10
        if command == "Quarantine":
            counter+=1
            if counter%2==0:
                print(f"{country} is already under quarantine")
        if command=="Cure":
            infection_dict[country]["persent"]=0


#for key,value in sorted(occ_dict.items(), key=lambda kvp:kvp[1], reverse=True):

for country, _ in infection_dict.items():
    for k, v  in sorted(infection_dict[country].items(),key=lambda kvp:kvp[1], reverse=True):
        print(f"{country} - {v}% infected")

