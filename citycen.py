city=input()
price=float(input())
res= None

if city=="Sofia":
    if price>=0 and price<=500:
        res=price*(5/100)
    elif price>500 and price<=1000:
        res=price*(7/100)
    elif price>1000 and price<=10000:
         res=price*(8/100)
    elif price>10000:
         res=price*(12/100)
    else:
        print('error')

elif city=="Varna":
    if price>=0 and price<=500:
        res=price*4.5/100
    elif price>500 and price<=1000:
        res=price*7.5/100
    elif price>1000 and price<=10000:
         res=price*10/100
    elif price>10000:
         res=price*13/100
    else:
        print('error')


elif city=="Plovdiv":
    if price>=0 and price<=500:
        res=price*5.5/100
    elif price>500 and price<=1000:
        res=price*8/100
    elif price>1000 and price<=10000:
         res=price*12/100
    elif price>10000:
         res=price*14.5/100
    else:
        print('error')
else:
    print('error')
if not res==None:
    print(f"{res:.2f}")
