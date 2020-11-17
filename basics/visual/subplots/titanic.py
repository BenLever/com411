import matplotlib.pyplot as plt
import csv

def read_data():
  titanic = {"survived":[], "sex":[], "age":[], "fare":[]}
  with open("basics/visual/subplots/train.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
      titanic["survived"].append(row[2])
      titanic["sex"].append(row[5])
      titanic["age"].append(row[6])
      titanic["fare"].append(row[10])
  
  return titanic

def run():
  data = read_data()
  fig, (ax1,ax2,ax3,ax4) = plt.subplots(2,2)
  ax1.plot(data["age","survived"])
  ax2.plot(data["sex","survived"])
  ax3.plot(data["age","fare"])
  ax4.plot(data["age","sex"])
  plt.show()

run()




  