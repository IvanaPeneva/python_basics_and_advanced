period_total_days=int(input())
starts_at=input().split(".")
d=int(starts_at[0])
m=int(starts_at[1])
y=int(starts_at[2])
a=d+period_total_days
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    if a>31:
        a=a-31
        m=m+1
        if m>12:
            y=y+1
    print(f"{a}.{m}.{y}")
elif m==4 or m==6 or m==9 or m==11:
    if a>30:
        a=a-30
        m=m+1
        if m>12:
            y=y+1
    print(f"{a}.{m}.{y}")
elif m==2:
    if y%4==0: #!!!! Modulno delene
        if a > 29:
            a = a - 29
            m = m + 1
            if m > 12:
                y = y + 1
        print(f"{a}.{m}.{y}")
    else:
        if a > 28:
            a = a - 28
            m = m + 1
            if m > 12:
                y = y + 1
        print(f"{a}.{m}.{y}")

else:
    print("INVALID MONTH")
