data=input().split(" -> ")
occ_dict={}
counter=0
while not data[0]=="login":
    username=data[0]
    password=data[1]
    occ_dict[username]=password
    data = input().split(" -> ")

log=input()
while not log=="end":
    users_password=log.split("  ")
    if users_password[0] in occ_dict.keys(): #vajno
        if occ_dict[users_password[0]]==users_password[2]: #ako v occ key suvpada s value ot input
            print("success")
        else:
            counter+=1
            print("fail")
    else:
        counter+=1
        print("fail")
    log=input()
print(f"{counter}")