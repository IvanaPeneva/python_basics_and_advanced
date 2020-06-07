import math
a=float(input())
b=float(input())
c=float(input())
volume_truck=a*b*c
n=int(input())
counter=0
for barrel in range(n):
    r=float(input())
    h=float(input())
    volume_barel=math.pi*r*r*h
    volume_truck=volume_truck-volume_barel

    if volume_truck<=0:
        print(f"Truck is full. {counter} on board!")
        exit(0)
    counter += 1
print(f"All barrels on board. Capacity left - {volume_truck:.2f}.")