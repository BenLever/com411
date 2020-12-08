from inhabitant import Inhabitant

class Robot:
  laws = "Protect, Obey and Survive"

  @staticmethod
  def the_laws(Inhabitant):
    print(Robot.laws)

  def __init__(self):
    self.name = "Robot"
    self.age = 0

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

if (__name__ == "__main__"):
  # create an object of type Human
  robot = Robot()

  # display the current state of the object
  print(repr(robot))