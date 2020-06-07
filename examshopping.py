data=list(input().split(" "))
occ_dict={}
while not data[0]=="shopping":
    product=data[1]
    quantity=int(data[2])
    if product in occ_dict.keys():
        occ_dict[product]+=quantity
    else:
        occ_dict[product]=quantity
    data=list(input().split(" "))

buy=input()
while not buy=="exam time":
    shopping_data=buy.split(" ")
    buy_product=shopping_data[1]
    buy_quantity=int(shopping_data[2])
    if buy_product not in occ_dict.keys():
        print(f"{buy_product} doesn't exist")
    elif occ_dict[buy_product]<=0:
        print(f"{buy_product} out of stock")
    else:
        occ_dict[buy_product]-=buy_quantity
    buy=input()

for key,value in occ_dict.items():
    if value>0:
        print(f"{key}==={value}")