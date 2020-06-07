data_list=list(map(int, input().split(" ")))
data_list.sort()
data_list=list(map(str,data_list))
print("k".join(data_list))


inp=input().split("|")
inp.reverse()
res=[]

for s in inp:
    s=s.split()
    res+=s
print(*res)

@property
    def age(self):
        return self.__age
@age.setter
    def age(self, value):   #veche dushterniq gleda settera na bashtiniq sus sushtoto ime
    Person.age.fset(self,value)_
        if value < 0:
            print("Age must be positive")
            exit(0)
        else:
            self.__age=value


try:
    a= Apartment("564a", 2, 4)
except Exception as ex:
    print(ex)