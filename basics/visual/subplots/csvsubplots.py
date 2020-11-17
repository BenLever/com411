import matplotlib.pyplot as plt
import csv

def read_data():
  temps = {"week1":[], "week2":[]}
  with open("basics/visual/subplots/temps.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
      temps["week1"].append(row[0])
      temps["week2"].append(row[1])
  
  return temps

def run():
  data = read_data()
  fig, (ax1,ax2) = plt.subplots(2,1)
  ax1.plot(data["week1"])
  ax2.plot(data["week2"])
  plt.show()

run()