from abc import ABC, abstractmethod

class Apartment(ABC):
    def __init__(self, id, rooms, baths, square_methers, price):
        self.id=id
        self.rooms=int(rooms)
        self.baths=int(baths)
        self.square_methers=float(square_methers)
        self.price=float(price)
        self.is_taken=False  #dobavqne na novo property

    @abstractmethod
    def __str__(self): #hvurlq greshka ako e samo e apartment
        return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.square_methers} sq. meters for {self.price} lv." #nov red

class LivingApartment(Apartment):
    def __init__(self, id, rooms, baths, square_methers, price):
        Apartment.__init__(self, id, rooms, baths, square_methers, price)

    def __str__(self):
       return Apartment.__str__(self) #vikane ot abctrakten bashta


class OfficeApartment(Apartment):
    def __init__(self, id, rooms, baths, square_methers, price):
        Apartment.__init__(self, id, rooms, baths, square_methers, price)


    def __str__(self):
       return Apartment.__str__(self)

data=input()
apartment_list=[]
while not data=="start_selling":
    try:
        current=eval(data)  #eval
        apartment_list.append(current)
    except Exception as ex:  #print Exception
        print(ex)
    data = input()

data_list=input().split()
ids_list=list(map(lambda a: a.id, apartment_list)) #a.id list samo ot id na vs v ap_list
while not (data_list[0]=="free" or data_list[0]=="taken"): #skobi zaradi not
    command=data_list[0]
    id=data_list[1]
    if id in ids_list:
        current: Apartment=list(filter(lambda a: a.id==id,apartment_list))[0] #vajno +tipizirane
        if current.is_taken:
            print(f"Apartment with id - {id} is already taken!")
        elif command=="rent" and isinstance(current, LivingApartment):
            print(f"Apartment with id - {id} is only  for selling!")
        elif command=="buy" and isinstance(current, OfficeApartment):
            print(f"Apartment with id - {id} is only for renting!")
        else:
            current.is_taken=True
    else:
        print(f"Apartment with id - {id} does not exist!")

    data_list = input().split()

if data_list[0]=="taken":
    taken_ap_list=list(filter(lambda a :a.is_taken==True,apartment_list)) #nov list samo ot is_taken
    for apartment in sorted(taken_ap_list, key=lambda acc: (acc.price, -acc.square_methers)):  # sortirane po 2 parametura nov parametur
        print(apartment)

elif data_list[0]=="free":
    taken_ap_list=list(filter(lambda a :a.is_taken==False,apartment_list))
    for apartment in sorted(taken_ap_list, key=lambda acc: (-acc.price, acc.square_methers)):  # sortirane po 2 parametura nov parametur
        print(apartment)

if len(taken_ap_list)==0:
    print("No information for this query")





