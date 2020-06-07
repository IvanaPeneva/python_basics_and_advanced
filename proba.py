while not data_list[0]=="report ":
    neighborhood,block_num =data_list[0].split("&") #Lozenec&2 -> 1|100000
    count_avaible, price=list(map(int,data_list[1].split("|"))) #int!
    block_num=int(block_num)

    if neighborhood in apartments.keys() and block_num in apartments[neighborhood].keys(): #vlizane v dict
        apartments[block_num]['availbale_count']=count_avaible #razpuvane i dobavqne v dict
        apartments[block_num]["price"]=price

    data_list = input().split(" -> ")

for neighborhood, _ in sorted(apartments.items(),key=lambda kvp:kvp[0]):
    print(f"Neighborhood: {neighborhood}")
    for block_num, info_dict in sorted(apartments[neighborhood].items(),key=lambda kvp:kvp[0]): #sort 2 dict
        #info_dict dvete stoinosti
        print(f"* Block number: {block_num} -> {info_dict['availbale_count']} apartments for sale. Price for one: {info_dict['price']}")

a=int(input())
for i in range(0,a,2):
    print(i)