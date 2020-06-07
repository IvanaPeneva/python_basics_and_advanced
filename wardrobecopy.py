n = int(input())

wardrobe_dict = {}

for iteration in range(n):
    data_list = input().split(' -> ')
    color = data_list[0]
    clothes = data_list[1].split(',')

    if color not in wardrobe_dict.keys():
        wardrobe_dict[color] = []

    wardrobe_dict[color].extend(clothes)

items_count_dict = {}

for color, clothes_list in wardrobe_dict.items():
    items_count_dict[color] = \
        {garment: clothes_list.count(garment)
         for garment in clothes_list}

data_list = input().split()
color_to_be_found = data_list[0]
clothes_to_be_found = data_list[1]

for color, kvp in items_count_dict.items():
    print(f"{color} clothes:")
    for garment, garment_count in kvp.items():
        if color_to_be_found == color and clothes_to_be_found == garment:
            print(f"* {garment} - {garment_count} (found!)")
        else:
            print(f"* {garment} - {garment_count}")