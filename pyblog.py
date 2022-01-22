# Example 1

"""
class Person:  # class declaration
    def __init__(self, name, age):  # constructor method
        self.name = name  # attributes
        self.age = age

    def set_age(self, new_age): # general methods
        self.age = new_age

mike = Person("Mike", 14)

print(mike.name) # Mike
mike.set_age(17)
print(mike.age) # 17
"""

# Example 2

"""
class Person:
    # class attribute
    class_name = "Person"

    def __init__(self, name, age):
        # instance attribute
        self.name = name
        self.age = age

mike = Person("Mike", 15)
print(mike.age) # 15
print(Person.class_name) # Person <- Accessing class variables using class
print(mike.__class__.class_name) # Person <- Accessing class variables using object
"""


# Example 3


"""
from datetime import date

class Person:
    class_name = "Person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def print_name(self):
        print(self.name)

    # class method
    @classmethod
    def create_person_from_birthyear(cls, name, birth_year):
        print("Creating a new object of type:", cls.class_name)
        return cls(name, date.today().year - birth_year)

    # static method
    @staticmethod
    def is_adult(age):
        return age > 18

mike = Person("Mike", 15)
mike.print_name() # Mike
james = Person.create_person_from_birthyear("James", 2001)
james.print_name() # James
Person.is_adult(james) # True
"""

# Example 4

"""
class Person:
    def __init__(self, name, age, salary):
        self.name = name  # public member
        self._age = age  # protected member
        self.__salary = salary  # private member


mike = Person("Mike", 17, 15000)
print(Mike.name) # Mike
print(Mike._age) # 17
print(Mike.__salary)  # Attribute Error

print(mike._Person__salary) # 15000
mike._Person__salary = 25000
print(mike._Person__salary) # 25000
"""

# Example 5

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read_age(self):
        print(self.age)


class Employee(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)  # can be Person.__init__(self, name, age)
        self.position = position
        self.salary = salary

    def read_salary(self):
        print(self.salary)


employee1 = Employee("Mike", 23, "Software Engineer", 999999)
employee1.read_age()  # 23 <- Method present in the parent class
employee1.read_salary()  # 999999 <- Method present in child class
"""


# Example 6

"""
class Vehicle:
    def print(self):
        print("This is parent class Vehicle")

class Car(Vehicle):
    def print(self):
        print("This is child class Car")

class Cycle(Vehicle):
    def print(self):
        print("This is child class Cycle")

vehicle = Vehicle()
car = Car()
cycle = Cycle()

vehicle.print() # This is parent class Vehicle <- Method called from Vehicle class
car.print() # This is child class Car <- Method called from Car class
cycle.print() # This is child class Cycle <- Method called from Cycle class
"""

# Example 7

"""
class Price:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        print("Price is", self.__price)

    def set_price(self, new_price):
        self.__price = new_price


amount = Price(-99)
amount.get_price()  # Price is -99
amount.set_price(99)
amount.get_price()  # Price is 99
print(amount.__price)  # Attribute Error <- evaluates to error as private members can't be accessed directly
"""

# Example 8
"""
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        pass


class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print("The changes from AnotherSubclass")


x = AnotherSubclass()
x.do_something()  # The changes from AnotherSubclass <- Implementation found in the child class
"""

# Example 9

"""
class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y >= 0:
            return "{}+{}i".format(self.x, self.y)
        else:
            return "{}{}i".format(self.x, self.y)

    def __add__(self, c):
        self.x = self.x + c.x
        self.y = self.y + c.y


c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(5, -3)
print(c1)  # 5+3i
print(c2)  # 5-3i
c1 + c2 # <- gets evaluated to c1.__add__(c2)
print(c1)  # 10+0i
"""
