from abc import ABC, abstractmethod

class BaseMonster(ABC):
    def __init__(self,name,id,strength,ugliness):
        self.name=str(name)
        self.id=int(id)
        self.strength=int(strength)
        self.ugliness=int(ugliness)

    @abstractmethod
    def __str__(self):
        return f"Overall speed of army: {self.speed}\nOverall strength: {self.strength}\nHydralisk: {self.count}; Zergling: {self.count}"


class Hydralisks(BaseMonster):
    def __init__(self,name,id,strength,ugliness,range):
        BaseMonster.__init__(self,name,id,strength,ugliness)
        self.range=str(range)

    def __str__(self):
       return BaseMonster.__str__(self)

class Zerglings(BaseMonster):
    def __init__(self,name,id,strength,ugliness,speed):
        BaseMonster.__init__(self,name,id,strength,ugliness)
        self.speed=int(speed)

    def __str__(self):
       return BaseMonster.__str__(self)

data=input()
army_list=[]
while not data=="stopAddingArmy":
    try:
        data = data.split('(')
        type_monster = data[0]
        data_monster = data[1].split(')')[0].split(", ")
        name_monster = data_monster[0].split('\'')[1]
        id = int(data_monster[1])
        strenght = int(data_monster[1])
        ugliness = int(data_monster[2])
    except Exception as ex:
        print(ex)
    data = input()


    #or
data = input()

while not data == 'stopAddingArmy':
    monster = {}
    data = data.split('(')
    type_monster = data[0]
    data_monster = data[1].split(')')[0].split(", ")
    name_monster = data_monster[0].split('\'')[1]
    id = int(data_monster[1])
    strenght = int(data_monster[1])
    ugliness = int(data_monster[2])
    if type_monster == 'Zergling':
        if len(data_monster) > 4:
            try:
                speed = int(data_monster[4])
                monster['name'] = name_monster
                monster['id'] = id
                monster['strength'] = strenght
                monster['ugliness'] = ugliness
                monster['speed'] = speed
                monster['type'] = 'Zergling'
                monsters.append(monster)
            except:
                print('Speed must be integer')
        else:
            print("__init__() missing 1 required positional argument: 'speed'")
    elif type_monster == 'Hydralisk':
        if len(data_monster) > 4:
            range_monster = data_monster[4].split('\'')
            if len(range_monster) > 1:
                monster['name'] = name_monster
                monster['id'] = id
                monster['strength'] = strenght
                monster['ugliness'] = ugliness
                monster['range'] = range_monster[1]
                monster['type'] = 'Hydralisk'
                monsters.append(monster)
            else:
                print('Range must be string')
        else:
            print("__init__() missing 1 required positional argument: 'range'")
    elif type_monster == "BaseMonster":
        print("Can't instantiate abstract class BaseMonster with abstract methods __init__")

    data = input()

count_z = 0
count_h = 0
overall_speed = 0
overall_strength = 0

for monster in monsters:
    if monster['type'] == 'Zergling':
        count_z += 1
        overall_speed += monster['speed']
    elif monster['type'] == 'Hydralisk':
        count_h += 1

    overall_strength += monster['strength']

print(f'Overall speed of army: {overall_speed}')
print(f'Overall stength: {overall_strength}')
print(f'Hydralisk: {count_h}; Zergling: {count_z}')
