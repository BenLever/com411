from inhabitant import Inhabitant

class Human(Inhabitant):

  def __init__(self, name, age, energy):

  def __str__(self):
    return f'My name is {self.__name} and I am {self.age} years old with {self.energy} energy.'

  def display(self):
    print(f"My name is {self.__name} and I am {self.age} years old with {self.energy} energy.")

if (__name__ == "__main__"):
  # create an object of type Human
  human = Human()

  # display the current state of the object
  print(str(human))
  