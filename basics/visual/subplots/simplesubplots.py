import matplotlib.pyplot as plt

def read_data(file_path):
  numbers = []
  with open("basics/visual/subplots/temps.txt") as file:
    for line in file:
      numbers.append(int(line.strip()))
  
  return numbers

def run():
  data = read_data("basics/visual/subplots/temps.txt")
  fig, axes = plt.subplots(2,2)
  axes[0,0].plot(data)
  plt.show()

run()