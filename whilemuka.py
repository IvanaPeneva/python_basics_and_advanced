name=input()
cap=int(input())
current=input()
counter=0

while name!=current:
    counter+=1
    current=input()
   
    if counter>=cap:
    
        print(f'The book you search is not here!')
        print(f'You checked {counter} books.')
        break
if counter<cap:
    print(f'You checked {counter} books and found it.')
