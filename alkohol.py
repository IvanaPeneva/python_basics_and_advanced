wisky=float(input())
lbira=float(input())
lwine=float(input())
lrakia=float(input())
lwisky=float(input())

rakia=wisky*0.5
wine=rakia-40/100*rakia
bira=rakia-80/100*rakia

sumarakia=rakia*lrakia
sumawine=wine*lwine
sumawisky=wisky*lwisky
sumabira=bira*lbira

obshto=sumarakia+sumawine+sumawisky+sumabira
print(f"{obshto:.2f}")

