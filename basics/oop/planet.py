class Robot:
  laws = "Protect, Obey and Survive"

  def the_laws():
    print(Robot.laws)

  def __init__(self):
    self.name = "Robot"
    self.age = 0

  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  Robot.the_laws()

class Human:
  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def grow(self):
    self.age += 1
  
  def eat(self):
    self.energy += 15

  def move(self):
    self.energy -= 10

  def display(self):
    print(f"I am {self.name} and I am {self.age} years old")
    print(f"Energy is {self.energy}")

if (__name__ == "__main__"):
  human = Human()
  human.display()
  human.grow()
  human.move()
  human.display()
  human.grow()
  human.move()
  human.display()
  human.eat()
  human.display()

class Planet:
  def __init__(self): 
    self.humans = []
    self.robots = []

  def add_human(self, human):
    self.humans.append(human)

  def remove_human(self, human):
    self.humans.remove(human)

  def add_robot(self, robot):
    self.robots.remove(robot)

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
  planet.add_human(person1)
  print(planet.__repr__())
  