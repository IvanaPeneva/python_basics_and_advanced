fruit=input()
day=input()
qua=float(input())
suma=None
if day=='Monday' or day=='Tuesday' or day=='Wednesday' or day=='Thursday' or day=='Friday':
    if fruit=='banana':
        suma=qua*2.50
    elif fruit=='apple':
        suma=qua*1.20
    elif fruit=='orange':
        suma=qua*0.85
    elif fruit=='grapefruit':
        suma=qua*1.45
    elif fruit=='kiwi':
        suma=qua*2.7
    elif fruit=='pineapple':
        suma=qua*5.5
    elif fruit=='grapes':
        suma=qua*3.85
  
elif day=="Saturday" or day=="Sunday":
     if fruit=='banana':
        suma=qua*2.70
    elif fruit=='orange':
        suma=qua*0.90
    elif fruit=='grapefruit':
        suma=qua*1.60
    elif fruit=='kiwi':
        suma=qua*3.00
    elif fruit=='pineapple':
        suma=qua*5.60
    elif fruit=='grapes':
        suma=qua*4.20
  

if result:
print(f"{suma:.2f}")
else:
    print('erorr')
