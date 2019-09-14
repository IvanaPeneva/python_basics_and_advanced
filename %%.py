n=int(input())
total1=0
total2=0
total3=0

for i in range (1,n+1):
    num=int(input())
    if num%2==0:
        total1+=1
    if num%3==0:
        total2+=1
    if num%4==0:
        total3+=1
        
p1=total1/n*100
p2=total2/n*100
p3=total3/n*100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
