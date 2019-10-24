import math

class Point:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Segment:
    
    def __init__(self, p1:Point, p2:Point):
        self.p1=p1
        self.p2=p2
        self.distance=self.calculator()
        
    def calculator(self):
        a=abs(self.p1.x-self.p2.x)
        b=abs(self.p1.y-self.p2.y)
        return math.sqrt(a ** 2 + b ** 2)
    
    def show(self):
        return f"{self.distance:.3f}\n({self.p1.x}, {self.p1.y})\n({self.p2.x}, {self.p2.y})"

def creator(x,y):
    point=Point(x, y)
    return point

n=int(input())
points_list=[]
for row in range(n):
    x, y=[int(num) for num in input().split()]
    point=creator(x,y)
    points_list.append(point)

segment_list=[]
for i1 in range(len(points_list)):
    for i2 in range(len(points_list)):
        if not i1==i2:
            segment=Segment(points_list[i1], points_list[i2])
            segment_list.append(segment)
            
for segment in sorted(segment_list, key=lambda s: s.distance):
    print(segment.show())
    break
    

