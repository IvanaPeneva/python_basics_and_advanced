import math
figure=input()
if figure=="rectangle":
    a=float(input())
    b=float(input())
    print(f"{a*b:.3f}")
if figure=="triangle":
    a=float(input())
    b=float(input())
    print(f"{a*b/2:.3f}")
if figure=="square":
    a=float(input())
    print(f"{a**2:.3f}")
if figure=="circle":
    a=float(input())
    print(f"{math.pi*(a**2):.3f}")


    
    
