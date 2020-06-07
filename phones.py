data=list(input().split(" : "))
occ_dict={}
while not data[0]=="Over":
    if data[1].isdigit():
        key=data[0]
        value=data[1]
        occ_dict[key]=value
    else:
        key=data[1]
        value=data[0]
        occ_dict[key] = value

    data =list(input().split(" : "))
for key,value in sorted(occ_dict.items()):
    print(f"{key} -> {value}")
