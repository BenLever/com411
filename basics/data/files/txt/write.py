def search(filepath):
  print("Searching...")
  sections = []
  books = []

  with open(filepath) as file:
    for line in file:
      if (line.startswith("Section")):
        split = line.split(":")
        sections.append(split[1][:-1])
      else:
        books.append(line[:-1])
  print("Done!")
  data = (sections,books)

  return data

def save(filepath,data):
  print("Saving...")

  with open(filepath,"w")as file:
    file.write(f"Sections: {data[1]}")
    file.write(f"Books: {data[1]}")
    print("Done!")

def run():
   data = search("basics/data/files/txt/books.txt")
   save("basics/data/files/txt/section-books.txt", data)

run()