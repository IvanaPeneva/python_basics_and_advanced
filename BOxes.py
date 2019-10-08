import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    @staticmethod
    def calculator(point_1, point_2):
        return math.sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)
   
    def show_info(self):
        return f"{self.x};{self.y}"

    
class Box:
    def __init__(self, upper_left:Point, upper_right:Point, bottom_left:Point, bottom_right:Point):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def get_width(self):
        width=Point.calculator(self.upper_left, self.upper_right)
        return width

        
    def get_hight(self):
        hight=Point.calculator(self.bottom_left, self.upper_left)
        return hight


    def perimeter(self):
        return 2*(self.get_hight() + self.get_width())


    def area(self):
        return self.get_hight()*self.get_width()
        
    def show_info(self):
        return f"Box: {self.get_width():.0f}, {self.get_hight():.0f}\nPerimeter: {self.perimeter():.0f}\nArea: {self.area():.0f}"
 
def create_point(coor):
    x, y = [int(num) for num in coor.split(":")]
    point = Point(x, y)
    return point
 
def create_box(u_l, u_r, b_l, b_r):
    upper_left = create_point(u_l)
    upper_right = create_point(u_r)
    bottom_left = create_point(b_l)
    bottom_right = create_point(b_r)
 
    box = Box(upper_left, upper_right, bottom_left, bottom_right)
    return box
 
   
 
 
data_list = input().split(" | ")
boxes_list = []
 
while not data_list[0] == "end":
    box = create_box(data_list[0], data_list[1], data_list[2], data_list[3])
    boxes_list.append(box)
   
    data_list = input().split(" | ")
 
 
for box in boxes_list:
    print(box.show_info())

  

















    
    
