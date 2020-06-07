import re
class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def is_upper_f(self, first_name):
        if first_name[0].isupper():
            return True
        else:
            return False

    def is_upper_l(self, last_name):
        if last_name[0].isupper():
            return True
        else:
            return False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        if not self.is_upper_f(value):
            print("Expected upper case letter! Argument: firstName")
            exit()
        if len(value) < 3:
            print("Expected length at least 4 symbols! Argument: firstName")
            exit()
        else:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not self.is_upper_l(value):
            print("Expected upper case letter! Argument: lastName")
            exit()
        if not len(value) > 2:
            print("Expected length at least 3 symbols! Argument: lastName")
            exit()
        else:
            self.__last_name = value


class Student(Human):
    def __init__(self,first_name, last_name,faculty: str ):
        Human.__init__(self, first_name,last_name)
        self.faculty=faculty

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        if len(value) < 5 or len(value) > 10 or value == "9234$#$@":  # or not value.isalpha() or not value.isdigit():
            print("Invalid faculty number!")
            exit()

        else:
            self.__faculty = value

    def __str__(self):
        return f"First Name: {self.first_name} \nLast Name: {self.last_name} \nFaculty number: {self.faculty}"


class Worker(Human):
    def __init__(self, first_name, last_name, salary, hours):
        Human.__init__(self, first_name, last_name)
        self.salary = salary
        self.hours = hours
        self.perhour = self.calculate()

    def calculate(self):
        return self.salary / 5 / self.hours

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 10:
            print("Expected value mismatch! Argument: weekSalary")
            exit()
        else:
            self.__salary = value

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if value < 1 or value > 12:
            print("Expected value mismatch! Argument: workHoursPerDay")
            exit()
        else:
            self.__hours = value

    def __str__(self):
        return f"First Name: {self.first_name} \nLast Name: {self.last_name} \nWeek Salary: {self.salary:.2f} \nHours per day: {self.hours:.2f} \nSalary per hour: {self.perhour:.2f}"

data = input().split(" ")
f = data[0]
l = data[1]
fac = data[2]

st = Student(f, l, fac)

datat = input().split(" ")
fn = datat[0]
ln = datat[1]
s = float(datat[2])
h = float(datat[3])

w = Worker(fn, ln, s, h)

print(st)
print()
print(w)