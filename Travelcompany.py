data=input()
city_dict={}
transport_dict={}
while not data=="ready":
    data_list=data.split(":")
    city=data_list[0]
    transport_list=data_list[1].split(",")
    if city not in city_dict.keys():
        city_dict[city]={}
    for item in transport_list:
        kvp=item.split("-")
        city_dict.get(city)[kvp[0]]=int(kvp[1]) #vajno dict_komprication
    data = input()

while True:
    travel=input()
    if travel=="travel time!":
        break
    passagers_list=travel.split()
    destination=passagers_list[0]
    passagers=int(passagers_list[1])
    transport_dict[destination]=passagers

for travel_city, people_count in transport_dict.items():
    sits = sum(city_dict.get(travel_city).values())  #vajno za da ne e s for

    if sits >= people_count:
        print(f'{travel_city} -> all {people_count} accommodated')
    else:
        total = people_count - sits
        print(f'{travel_city} -> all except {total} accommodated')
