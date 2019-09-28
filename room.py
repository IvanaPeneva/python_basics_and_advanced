days=int(input()) - 1
room=input()
grade=input()

res=0
if room=='room for one person':
    res=18*days
elif room=='apartment':
    if days<10:
        res=25*days*70/100
    elif days>=10 and days<=15:
        res=25*days*0.65
    else:
        res=25*days*0.50
        
elif room=='president apartment':
    if days<10:
        res=35*days*90/100
    elif days>=10 and days<=15:
        res=35*days*0.85
    else:
        res=35*days*0.80

if grade=='positive':
    res=res*1.25
elif grade=='negative':
    res*=0.9
print(f"{res:.2f}")
