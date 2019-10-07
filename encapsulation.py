class Person:
    def __init__ (self, name:str, age:int):
        self.name=name
        self.age=age
    @property #props 
    def age(self):
        return self.__age


    @age.setter
    def age(self, value):
        if value<0:
            print("Age must be positive")
        else:
            self.__age=value
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
        
    @property #props 
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        if len(value)<3 :
            print(f"Name's length should not be less than 3 symbols!")
        else:
            self.__name=value
            
class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name,age)
        

        
    @property #props 
    def age(self):
        return self.__age


    @age.setter
    def age(self, value):
        if value>=15:
            print("Child's age must be less than 15!")
        if value<0 and len(name)>3:
            print ("Age must be positive!")
        else:
            self.__age=value


name=input()
age=int(input())
user=Child(name, age)
if age<15 and age>0 and len(name)>=3:
    print(user)



#person= Person("Ines", 25)        
#chl=Child("Pikachu", -3)
#print(chl)

            


