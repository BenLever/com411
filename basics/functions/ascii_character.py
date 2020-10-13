print("Program Started!")
print("Please enter an ASCII code:")
ascii = int(input())

if(32<=ascii<=126):
  letter = chr(ascii)
  print("The character represented by the ASCII code {} is: {}".format(ascii,letter))
  print("Program Ended!")

elif not(32<=ascii<=126):
  print("Please enter an ASCII code in the range 32-126")