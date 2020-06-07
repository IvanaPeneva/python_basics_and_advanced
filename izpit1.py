import math
days=int(input())
courses=float(input())
hours=int(input())
totalh=courses*hours

learn=0
for day  in range(1,days+1):
    if day % 2==0 or day % 10==0:
        learn+=4

    elif day % 5==0:
        learn+=2

    else:
        learn+=1

result=learn-totalh
result_1=totalh-learn
pr=math.ceil(result_1/hours)

if result>=0:
    print(f"You watched all the courses and are left with {result:.0f} free hours")
else:
    print(f"You need to complete {pr:.0f} more courses")

