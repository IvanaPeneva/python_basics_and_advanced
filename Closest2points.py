import math

class Point:
    def __init__(self, x, y):
        self.x=int(x)
        self.y=int(y)

class Segment:
    def __init__(self, p1:Point, p2:Point):
        self.p1=p1
        self.p2=p2
        self.distance=self.calculate_distance() #vlzane vuv funkzia

    def calculate_distance(self): #shtom e v klasa samo self
        delta_x=abs(self.p2.x-self.p1.x)  #dobavqne na self.
        delta_y=abs(self.p2.y-self.p1.y)
        return math.sqrt(delta_x**2 +delta_y**2)

    def show_info(self):
        return f"{self.distance:.3f}\n({self.p1.x},{self.p1.y})\n({self.p2.x},{self.p2.y})"


def create_point(x,y):
    point=Point(x,y)
    return point


n=int(input())
points_list=[]
segment_list=[]
for row in range(n):
    x, y = list(map(int, input().split())) #or x,y=[int(num) for num in input().split()]
    point=create_point(x,y) #tva e ot gorniq red
    points_list.append(point)
for index_1 in range(len(points_list)):
    for index_2 in range(len(points_list)):
        if not index_1==index_2:
            segment=Segment(points_list[index_1],points_list[index_2])
            segment_list.append(segment)
for segment in sorted(segment_list,key=lambda s: s.distance):
    print(segment.show_info())
    break

