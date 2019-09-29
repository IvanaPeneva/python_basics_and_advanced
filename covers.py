num=int(input())
lengh=float(input())
width=float(input())
covers=num*(lengh+2*0.30)*(width+2*0.30)
squ=num*(lengh*0.5)**2
dollars=covers*7+squ*9
leva=dollars*1.85
print(f"{dollars:.2f} USD")
print(f"{leva:.2f} BGN")
