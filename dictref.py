data=input().split(" = ")
occ_dict={}
while not data[0]=="end":
    if data[1].isdigit():
        key=data[0]
        value=int(data[1])
        occ_dict[key]=value
    else:
        if data[1] in occ_dict.keys():
            occ_dict[data[0]]=occ_dict[data[1]]  #vajno

    data = input().split(" = ")
for key,value in occ_dict.items():
    print(f"{key}->{value}")

