surch_key=input().lower()
surch_value=input().lower()
N=int(input())
occ_dict={}
for string in range(N):
    string=input().lower().split(" => ")
    given_key=string[0]
    given_value=string[1].split(";")
    occ_dict[given_key]=given_value
for given_key, given_value in occ_dict.items():
    if surch_key in given_key:
        print(f"{given_key}:")
        for el in occ_dict[given_key]:
            if surch_value in el:
                print(f"-{el}")