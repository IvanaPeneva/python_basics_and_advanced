import math
data=input().split(" ")
shell_dict={}
while not data[0]=="Aggregate":
    region=data[0]
    shell=data[1]

    if region not in shell_dict.keys():
        shell_dict[region]=shell
    else:
        if shell in shell_dict[region]:
            data=input().split(" ")
            continue
        else:
            shell_dict[region]= shell_dict[region]+ ", " + shell #.append(shell)
    data=input().split(" ")
counter=0
for key, value in shell_dict.items():
    counter=0
    suma=0
    a=value.split(", ")
    for el in a:
        elem=int(el)
        suma+=elem
        counter+=1
    big_shell=suma-suma/counter
    print(f"{key} -> {value} ({math.ceil(big_shell)}) ")
