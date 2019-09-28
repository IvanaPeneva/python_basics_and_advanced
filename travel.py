budj=float(input())
sezon=input()

where=None
contry=None
res=0

if budj<=100:
    contry='Bulgaria'
    if sezon=='summer':
        res=30/100*budj
    elif sezon=='winter':
        res=70/100*budj
elif budj<=1000:
    contry='Balkans'
    if sezon=='summer':
        res=40/100*budj
    elif sezon=='winter':
        res=80/100*budj
elif budj>1000:
    contry='Europe'
    if sezon=='summer' or sezon=='winter':
        res=90/100*budj

if sezon=='summer':
    where='Camp'
elif sezon=='winter':
    where='Hotel'
if contry=='Europe':
    where='Hotel'

print(f'Somewhere in {contry}')
print(f'{where} - {res:.2f}')
