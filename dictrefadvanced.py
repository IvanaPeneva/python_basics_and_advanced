data=input().split(" -> ")
names_dict={}
while not data[0]=="end":
    name=data[0]
    item=data[1].split(", ")
    if item[0].isdigit():
        if name not in names_dict.keys():
            names_dict[name]=[]
        names_dict[name].extend(item)
    else:
        if item[0] in names_dict.keys():
            if name not in names_dict.keys():
                names_dict[name]=[]
            names_dict[name].extend(names_dict[item[0]]) #vajno extend s stoinost

    data = input().split(" -> ")
#ediniq dict e razlichen ot drugiq
for key, value in names_dict.items():
    a=", "
    print(f"{key} === {a.join(value)} ")