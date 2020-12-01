class Robot:
  laws = "Protect, Obey and Survive"

  def the_laws():
    print(Robot.laws)

  def __init__(self):
    self.name = "Robot"
    self.age = 0

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

class Human:
  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def __str__(self):
    return f'My name is {self.__name} and I am {self.age} years old.'


