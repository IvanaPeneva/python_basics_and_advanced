import math
L=float(input())
W=float(input())
A=float(input())
obem=(L*100)*(W*100)
gard=(A*100)**2
peika=obem/10
svob=obem-gard-peika
numdance=svob/(40+7000)
print(math.floor(numdance))
