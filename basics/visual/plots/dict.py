import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}
  print("What type of line would you like to use? (:, -- or -)")
  linetype = str(input())
  print("What colour would you like? (r, g or b)")
  colour = str(input())
  print("What style of marker would you like? (o, s or ^)")
  style = str(input())

  paths['linetype'] = linetype
  paths['colour'] = colour
  paths['style'] = style
  return paths

def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  for num_line in range(num_lines):
    d = data()
    
    x = [0, rnd.randrange(1, 10)]
    y = [0, rnd.randrange(1, 10)]

    plt.plot(x, y, f"{d['colour']}{d['linetype']}{d['style']}")
  
  plt.show()

def run():
  print("Running...")
  generate()
  print("Done!")

run()
