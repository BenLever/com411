print("Program Started!")
print("Please enter a standard character")
letter = str(input())

if len(letter) == 1:
  ASCII = ord(letter)
  print("The ASCII code for {} is {}".format(letter,ASCII))
  print("Program Ended!")

elif len(letter) != 1:
  print("Please enter a single letter")