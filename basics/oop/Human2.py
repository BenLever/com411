from inhabitant import Inhabitant

class Human(Inhabitant):

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY

  def __repr__(self):
    return f'human(name={self.name}, age={self.age})'
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old with {self.energy} energy.'

  def display(self):
    print(f"My name is {self.name} and I am {self.age} years old with {self.energy} energy.")

if (__name__ == "__main__"):
  # create an object of type Human
  human = Human("Ben", 19)
  human.grow()
  print(human)

  # display the current state of the object
  print(str(human))
  

  
