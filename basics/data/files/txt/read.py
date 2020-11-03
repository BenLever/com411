def search(filepath):
  print("Searching...")
  
  with open(filepath) as file:
    for line in file:
      print(f"Looked in {line}")
  print("...Done!")

def run():
  search("basics/data/files/txt/locations.txt")

run()