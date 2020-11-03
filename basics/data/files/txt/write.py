def search(filepath):
  print("Searching...")
  sections = []
  books = []

  with open(filepath) as file:
    for line in file:
      if line.startwith("Section"):
        split = line.split(:)
        sections.append(split[1][:-1])
      else:
        books.append(line[:-1])
  print("Done!")
  data = (sections,books)

  return data

def save(filepath,data):
  print("Saving...")
  sections = ""
  books = ""

  with open(filepath,"w")as file:
    sections =+ "Sections: "
    for section in data[0]
      sections += section [-1] +","
    books += "Books: "
    for book in data[1]
      books = book +","

    file.write(sections[:-2])
    file.write(books[:-2])
    print("Done!")

def run()
   data = search("basics/data/files/txt/book.txt")
   data2 = save("basics/data/files/txt/section-books.txt")

run()