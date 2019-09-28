plant=input()

is_fruit= plant=='banana'or plant=='apple'or plant=='kiwi' or plant=='cherry'or plant=='lemon' or plant=='grapes'
    
is_vegetable= plant== 'tomato' or plant=='cucumber'or plant=='pepper' or plant=='carrot'
   
if is_fruit:
    print("fruit")
elif is_vegetable:
    print("vegetable")
else:
    print("unknown")
    
