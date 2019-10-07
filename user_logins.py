data_list=list(input().split(" -> "))
dictionary={}
while not data_list[0]=="login":
    key=data_list[0]
    value=data_list[1]
    dictionary[key]=value
    data_list=list(input().split(" -> "))
    counter=0
    log = list(input().split(" -> "))
    while not log[0] == "login":
        if key==log[0] and value==log[1]:
            print(f'{key}: logged in successfully.')
        else:
            print(f'{key}: login failed.')
            counter+=1
        if log=="end":
            print(f'unsuccessful login attempts: {counter}')
        log = list(input().split(" -> "))
