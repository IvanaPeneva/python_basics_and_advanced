proj=input()
r=int(input())
c=int(input())

res=0
if proj=="Premiere":
    res=12*r*c
elif proj=="Normal":
    res=7.5*r*c
elif proj=='Discount':
    res=5*r*c

    
print(f"{res:.2f} leva")
