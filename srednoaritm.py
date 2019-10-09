n=int(input())
command=input()
counter=0
kraina=0
while command!="Finish":
    suma=0
    for i in range(n):
        ocenka=float(input())
        suma+=ocenka
    sredno=suma/n   
    print(f"{command} - {sredno:.2f}.")
    counter+=1
    kraina+=sredno
    command=input()
    
final=kraina/counter

print(f"Student's final assessment is {final:.2f}.")
        

    
    
