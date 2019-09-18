class Person:
    """class to represent a person
    """
    def __init__(self):
        self.name =''
        self.age = 0
    def display(self):
        print("Person ('%s', '%d')" % (self.name, self.age))
            
#> p=Person()
#>>> p.display()
#Person ('', '0')
#>> p.name='Bob'
#>>> p.age= 23
#>>> p.display()
#Person ('Bob', '23')
