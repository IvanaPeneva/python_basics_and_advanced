import math

class Point:
    def __init__(self, x, y):
        self.x=int(x)
        self.y=int(y)

#printirane na tochki ne e kum zadachata
sample_point=Point(2, 3)
print(f"{sample_point.x}, {sample_point.y}")


def calculate_distance(p1:Point, p2:Point): #dobavqne na : kum class
    delta_x=abs(p2.x-p1.x)
    delta_y=abs(p2.y-p1.y)
    return math.sqrt(delta_x**2 +delta_y**2)


def create_point(x,y):
    point=Point(x,y)
    return point

x_1, y_1=list(map(int,input().split()))  # or data=input().split()
x_2, y_2=list(map(int,input().split()))
point_1=create_point(x_1, y_1)
point_2=create_point(x_2, y_2)
distance=calculate_distance(point_1, point_2)
print(f"{distance:.3f}")