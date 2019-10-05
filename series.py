budj=int(input())
n=int(input())
counter=0
total=0

for i in range(n):
    name=input()
    cena=float(input())
    if name=="Thrones":
        cena=cena-50/100*cena
        counter+=1
        total+=cena
    elif name=="Lucifer":
        cena=cena-40/100*cena
        counter+=1
        total+=cena
    elif name=="Protector":
        cena=cena-30/100*cena
        counter+=1
        total+=cena
    elif name=="TotalDrama":
        cena=cena-20/100*cena
        counter+=1
        total+=cena
    elif name=="Area":
        cena=cena-10/100*cena
        counter+=1
        total+=cena
    else:
        cena=cena
        counter+=1
        total+=cena
if budj>=total:
    ost=budj-total
    print(f"You bought all the series and left with {ost:.2f} lv.")
else:
    nujni=total-budj
    print(f"You need {nujni:.2f} lv. more to buy the series!")
    
