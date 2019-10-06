import math


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

        
class Povedenie:
    def __init__(self, point_1:Point,point_2:Point):
        self.point_1=point_1
        self.point_2=point_2
        self.distance=self.calculate()

        
    def calculate(self):
        a=abs(self.point_1.x-self.point_2.x)
        b=abs(self.point_1.y-self.point_2.y)
        c=math.sqrt(a**2+b**2)
        return c
    def show(self):
        return f"{self.distance:.3f}\n({self.point_1.x}, {self.point_1.y})\n({self.point_2.x}, {self.point_2.y})"
def creator(x,y):
    point=Point(x,y)
    return point

n=int(input())
point_list=[]
povedenie_list=[]
for row in range(n):
    x,y=[int(num) for num in input().split()]
    point=creator(x,y)
    point_list.append(point)

for index_1 in range(len(point_list)):
    for index_2 in range(len(point_list)):
        if not index_1==index_2:
            povedenie=Povedenie(point_list[index_1], point_list[index_2])
            povedenie_list.append(povedenie)
for povedenie in sorted(povedenie_list, key=lambda s:s.distance):
    print(povedenie.show())
    break

            



    

    
    
    


