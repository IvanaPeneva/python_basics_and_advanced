budj=int(input())
sezon=input()
broi=int(input())
res=0
if sezon=='Spring':
    res=3000
    if broi<=6:
        res*=0.9
    elif broi>=7 and broi<=11:
        res*=0.85
    else:
        res*=0.75
elif sezon=='Summer' or sezon=='Autumn':
    res=4200
    if broi<=6:
        res*=0.9
    elif broi>=7 and broi<=11:
        res*=0.85
    else: 
        res*=0.75
else:
    res=2600
    if broi<=6:
        res*=0.9
    elif broi>=7 and broi<=11:
        res*=0.85
    else:
        res*=0.75
    

    
if broi %2 ==0 and sezon!='Autumn':
    res*=0.95
   
if budj>=res:
    print(f"Yes! You have {budj-res:.2f} leva left.")
else:
    print(f"Not enough money! You need {res-budj:.2f} leva.")
    
