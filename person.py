# the class i.e. blueprint for my objects
class Person:

  #Class attribute--->constant, sisible to all objects of the class
  MAX_ENERGY=100

#Initializer ( special instance method , invoked only once at creation)
  def __init__(self, name, age=0, weight=10, energy=100):
    #Instance attributes 
    self.name = name
    self.age = age
    self.weight = weight
    if energy > 100:
      self.energy = Person.MAX_ENERGY
    else:
      self.energy = energy

  def hello(self): 
    print(f"Hello my name is {self.name}. I'm {self.age} years old and I weight {self.weight} kg. Nice to meet you!")
#3. 
  def grow(self):
    self.age +=1
#4.
  def eat(self, food, weight):
    self.weight +=weight
    print(f"{self.name} have eaten {food} and now weights {self.weight}")

if __name__ == "__main__":
#1. Person.MAX_ENERGY = 50
 Piotr = Person("Piotr",66,81,65)
 Anca = Person("Anca", 18)
 Mihai = Person("Mihai")
 Tim = Person("Tim",weight=87)
#2.
#  
#1. print(f"person 1 is called {person1.name} and person2 is called {person2.name}. The combined weight is : {person1.weight + person2.weight}")


#1. print(f"Person 1 has {person1.energy} energy and Person 2 has {person2.energy} energy, and Person 3 has {person3.energy} energy.")

#2.print(f"The age of Piotr : {Piotr.age}, Anca's age : {Anca.age},and Tim's age is : {Tim.age} years old ")

# 3.
Anca.hello()
Tim.hello()
Piotr.hello()
Mihai.hello()

# Piotr.grow()
# Piotr.hello()

#4.
# Tim.hello()
# Tim.eat("Lasagne", 2 )
# Tim.hello() 