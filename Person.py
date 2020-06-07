class Person:
    def __init__(self, name :str, age :int):
        self.name=name
        self.age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age must be positive")
            exit(0)
        else:
            self.__age=value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            print("Name's length should not be less than 3 symbols!")
            exit(0)
        else:
            self.__name = value
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Person.age.fset(self, value) #fset
        if value > 15:
            print("Child's age must be less than 15!")
            exit(0)
        #if value<0:
            #print("Age must be positive")
            #exit(0)
        else:
            self.__age=value

    #def __str__(self):
        #return f"Name: {self.name}, Age: {self.age}"

#ako ima property sus suchtoto ime v negoviq class gleda samo nego
person=Person("Preso", 25)
child=Child("Ki", -3)
print(child)
print(person)