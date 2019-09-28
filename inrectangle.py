x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x=float(input())
y=float(input())

is_x_in = x1<=x and x<=x2
is_y_in = y1<=y and y<=y2

is_inside=is_x_in and is_y_in

if is_inside:
    print("Inside")
else:
    print("Outside")
     
