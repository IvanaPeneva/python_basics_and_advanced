n=int(input())
m=float(input())
counter=0
for l_i in range(n):
    mess=input()
    location=''
    if mess.isdigit():
        for i in range(0,len(mess)-1, 2): #za edna stupka
            num_pair=int(mess[i]+mess[i+1])
            char=chr(num_pair)
            location+=char
        print(f'Reviewing item – {location}')
        counter+=1

    elif mess.isalpha():
        location=mess[::-1]
        print(f"Reviewing location – {location}")
        counter+=1
salary=counter*m
print(f"{counter} reviews have been made this month. Salary: {salary}")
