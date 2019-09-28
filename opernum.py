n1=int(input())
n2=int(input())
oper=input()

chetno='even'

if oper=='+':
    res=n1+n2
    if res%2 !=0:
        chetno='odd'
    print(f"{n1} {oper} {n2} = {res} - {chetno}")

elif oper=='-':
    res=n1-n2
    if res%2 !=0:
        chetno='odd'
    print(f"{n1} {oper} {n2} = {res} - {chetno}")

        
elif oper=='*':
    res=n1*n2
    if res%2 !=0:
        chetno='odd'
    print(f"{n1} {oper} {n2} = {res} - {chetno}")

elif oper=='/':
    if n2=='0':
        print(f'Cannot divide {n1} by zero')
    res=n1/n2
    print(f"{n1} / {n2} = {res}")
              
elif oper=='%':
    if n2==0:
        print(f'Cannot divide {n1} by zero')
    else:
        res=n1%n2
        print(f'{n1} % {n2} = {res}')

