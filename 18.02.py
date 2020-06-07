data=list(map(int, input().split()))
command=input()
while not command=="END":
    coma=command.split()
    if coma[0]=="multiply":
        if coma[1]=="list":
            n=int(coma[2])
            data=data*n

        elif coma[1].isdigit():
            element=int(coma[1])
            n=int(coma[2])
            data=[a*n if element==a else a for a in data]
            #data=list(map(lambda a: a*n if a==element else a, data))
    elif coma[0]=="contains":
        element=int(coma[1]) #int!
        if element in data:
            print("True")
        else:
            print("False")
    elif coma[0]=="add":
        addition=coma[1].split(",")
        for el in addition:
            el=int(el)
            data.append(el)

    command=input()

#print(" ".join(map(str,sorted(data))))

#data.sort()
#print(*data)
for num in sorted(data):
    print(num, end=" ")