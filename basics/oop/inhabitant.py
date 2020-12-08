class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY
    
  def grow(self):
    self.age += 1

  def eat(self, amount):
    if self.energy + amount > Inhabitant.MAX_ENERGY:
      print("Cannot increase energy above max")
    else:
      self.energy += amount

  def move(self, amount):
    if self.energy - amount <= 0:
      print("Can't move")
    else:
      self.energy -= amount



