typ=input()
broi=int(input())
budj=int(input())

res=0
if typ=='Roses':
    res=5*broi
    if broi>80:
        res=res*0.9
elif typ=='Dahlias':
    res=3.80*broi
    if broi>90:
        res*=0.85
elif typ=='Tulips':
    res=2.8*broi
    if broi>80:
        res*=0.85
elif typ=='Narcissus':
    res=3*broi
    if broi<120:
        res=res*15/100+res
elif typ=='Gladiolus':
    res=2.5*broi
    if broi<80:
        res=res*2/10+res
ost=budj-res
if ost>=0:
    print(f"Hey, you have a great garden with {broi} {typ} and {ost:.2f} leva left.")
else:
          print(f"Not enough money, you need {res-budj:.2f} leva more.")
