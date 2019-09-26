day=int(input())
slatkar=int(input())
cake=int(input())
gofr=int(input())
pan=int(input())
cake_pr=cake*45
gofr_pr=gofr*5.80
pan_pr=pan*3.20
for1day=(cake_pr+gofr_pr+pan_pr)*slatkar
obshto=for1day*day
aftertax=obshto-obshto*1/8
print(f"{aftertax:.2f} ")
