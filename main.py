def gang():
  print("Loading gang...")
  friends = ["Scooby Doo",
  "Shaggy Rogers",
  "Fred Jones",
  "Daphne Blake",
  "Velma Dinkley"
  ]
  print(friends)
  print("...Done!")
  return friends

gang()

def gang():
  friends = ["Scooby Doo",
  "Shaggy Rogers",
  "Fred Jones",
  "Daphne Blake",
  "Velma Dinkley"
  ]
  return friends

def phrases(friends):
  quotes = {}
  for friend in friends:
    print(f"What does {friend} say?")
    quote = str(input())
    quotes.update({friend:quote})
  return quotes

friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n")

def save(quotes):
  with open(quotes.txt, "w")as file:
    for friend, quote in quotes.item():
      file.write(f"{friend}:{quote}")

save(quotes) 
print("The file contains...")
file = open("quotes.txt")
print(file.read())
file.close()

