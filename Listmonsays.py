numbers=list(map(int, input().split()))
data_list=input()
counter=0
while not data_list=="exhausted":
    manipulated=[]
    data=data_list.split()
    command=data[0]
    if command=="set":
        if len(set(numbers))==len(numbers):
            print(f"It is a set")
        else:
            manipulated=list(sorted(set(numbers), key=numbers.index))

    elif command=="filter":
        if data[1]=="even":
            manipulated=[num for num in numbers if num % 2 ==0]

        elif data[1]=="odd":
            manipulated = [num for num in numbers if num % 2 == 1]

    elif command =="multiply":
        n=int(data[1])
        manipulated=list(map(lambda el:el*n, numbers))

    elif command =="divide":
        n = int(data[1])
        if n==0:
            print("ZeroDivisionError caught")
        else:
            manipulated = list(map(lambda el: el / n, numbers))

    elif command =="slice":
        n=int(data[1])
        m=int(data[2])
        if (n>=0 and n<len(numbers)and m>=0 and m<len(numbers) and n<m):
            manipulated=numbers[n:m+1]
        else:
            print("IndexError caught")

    elif command == "sort":
        manipulated=list(sorted(numbers))

    elif command == "reverse":
        manipulated=list(reversed(numbers))

    if len(manipulated) > 0:
        print(manipulated)

    counter+=1

    data_list = input()
print(f"I beat It for {counter} rounds!")
