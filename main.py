class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Joey", "King", 2021)
x.printname()
print(x.graduationyear)


#import neccessary package
from abc import ABC,abstractmethod
#create a base class
class animal (ABC):
    
    #Abstract method 
      #sgould be implemented by all sub-classes
      def move(self):
               pass

class Animal:
    def move(self):
        print("I can move")

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

# Driver code
R = Human()
R.move()  # Output: I can walk and run

K = Snake()
K.move()  # Output: I can crawl

R = Snake()
R.move()  # Output: I can crawl

K = Dog()
K.move()  # Output: I can bark


