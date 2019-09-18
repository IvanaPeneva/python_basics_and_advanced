class Person:
    def display(self):
        print( "Person (name, age)" % (self.name, self.age))
    def __str__(self):
        return "Person (name, age)" % (self.name, self.age)
    
