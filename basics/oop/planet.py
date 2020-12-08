from inhabitant import Inhabitant
from Human2 import Human
from Robot import Robot

class Planet:
  def __init__(self): 
    self.inhabitants = []

  def add(self, inhabitants):
    self.inhabitants.append(Inhabitant)

  def remove(self, human):
    self.inhabitants.remove(Inhabitant)


  def __str__(self):
    return f"{self.humans}"
    return f"{self.robots}"
  def __repr__(self):
    return self.humans, self.robots

if (__name__ == "__main__"):
  planet = Planet()
  planet.__str__()
  planet.__repr__()
  person1 = Human()
  planet.add(person1)
  print(planet.__repr__())
  