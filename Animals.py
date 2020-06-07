#from abc import ABC, abstractmethod
class Animal:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    #@abstractmethod
    #def make_sound(self):
    #   pass

class Dog(Animal):
    #def make_sound(self):
    #   return "bau bau"
    def __init__(self,name,age,number_legs:int):
        Animal.__init__(self,name,age)
        self.number_legs=number_legs
    def make_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_legs}" #pise se self

class Cat(Animal):
    #def make_sound(self):
    # return "bau bau"
    def __init__(self,name,age,IQ:int):
        Animal.__init__(self,name,age)
        self.IQ=IQ
    def make_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, IQ: {self.IQ}"


class Snake(Animal):
    def __init__(self,name,age,CC:int):
        Animal.__init__(self,name,age)
        self.CC=CC
    def make_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."
    def __str__(self):
        return f"Snake: {self.name}, Age: {self.age}, Cruelty: {self.CC}”"
data=input().split()
animals_list=[]
while not data[0]== "I'm":
    if data[0]=="talk":
        name=data[1]
        current=list(filter(lambda a :a.name==name, animals_list)) [0] #ot list vzemam purvoto
        print(current.make_sound())
    else:
        kind=data[0]
        name=data[1]
        age=data[2]
        paramether=data[3]
        if kind=="Dog":
            dog=Dog(name,age,paramether)
            animals_list.append(dog)
        elif kind=="Cat":
            cat=Cat(name,age,paramether)
            animals_list.append(cat)
        elif kind=="Snake":
            snake=Snake(name,age,paramether)
            animals_list.append(snake)
    data = input().split()

#ima sortirovka s lambda v papkata: dogs_list=filter(lambda x :x isinstance(x, Dog),animals_list)
for animal in animals_list: #raboti s __str__
    print(animal)
#print(cat.make_sound) != print(dog.make_sound) abstract