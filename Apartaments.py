apartments={} #1
data_list=input().split(" -> ")
while not data_list[0]=="collectApartments":
    neighborhood=data_list[0]
    bloks_nums=list(map(int,data_list[1].split(",")))
    if neighborhood not in apartments.keys():
        apartments[neighborhood]={} #2
    for num in bloks_nums:
        apartments[neighborhood][num]={'available_apartments_count':0, "price":None} #nqkolko rechnika v 1 #3

    data_list = input().split(" -> ")

data_list=input().split(" -> ")
while not data_list[0].strip() == 'report':
    neighborhood, block_num = data_list[0].split('&') ##Lozenec&2 -> 1|100000
    count_available, price = list(map(int, data_list[1].split('|')))
    block_num = int(block_num) #int

    if neighborhood in apartments.keys() and block_num in apartments[neighborhood].keys():
        apartments[neighborhood][block_num]['available_apartments_count'] = count_available #razpuvane i dobavqme v dict
        apartments[neighborhood][block_num]['price'] = price

    data_list = input().split(' -> ')

for neighborhood, _ in sorted(apartments.items(), key=lambda kvp: kvp[0]):
    print(f"Neighborhood: {neighborhood}")
    for block_num, info_dict in sorted(apartments[neighborhood].items(), key=lambda kvp: kvp[0]): #sort 2ri dict
        # info_dict dvete stoinosti
        print(
            f"* Block number: {block_num} -> {info_dict['available_apartments_count']} apartments for sale. Price for one: {info_dict['price']}")

