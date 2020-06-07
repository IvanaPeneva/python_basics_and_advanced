a_list=["a", "b", "c", "a"]
filtered_a=sorted(set(a_list),key=lambda x: a_list.index(x))
print(filtered_a) #removes a

b_list=["3", "4", "1", "2"]
b_list.sort()
print(b_list)
b_list.sort(reverse=True)
print(b_list)


c_list=a_list[::-1] #reverse
print(c_list)
#https://www.w3schools.com/python/python_howto_remove_duplicates.asp
#remove dublicates