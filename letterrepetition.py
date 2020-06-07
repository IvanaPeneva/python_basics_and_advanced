data=input()
occ_dict={num:data.count(num) for num in data}
for key,value in occ_dict.items():
    print(f"{key}={value}")
