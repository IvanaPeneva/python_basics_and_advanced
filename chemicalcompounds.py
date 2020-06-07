data=list(map(int, input().split(", ")))
inp=input()

searched_el=[]
remaining_el=[]
taken_indexes=[]
total_compound=0
error=False

while not inp=="end":
    inp_index = list(map(int, inp.split("-")))
    for el in inp_index:
        if el >=len(data):
            print("Invalid indices")
            searched_el=[] #izprazvane na lista vs neuspeshen put
            error=True
            break
        elif int(el) in taken_indexes:
            print(f"Index {el} is already taken")
            searched_el=[]
            error=True
            break
        else:
            searched_el.append(data[el]) # index-> chislo

    if error==False:
        print(f"Found compound: {searched_el}")
        total_compound+=1
        searched_el=[] #izpazvane na lista sled kraq
        taken_indexes+=inp_index
    else:
        error=False

    inp=input()

print(f"Total compounds: {total_compound}")
for i in range(len(data)):
    if i not in taken_indexes:
        remaining_el.append(data[i])
print(f"Elements left: {remaining_el}")

    #if max(indexes_1)>len(data):
        #print(f"Invalid indices")
