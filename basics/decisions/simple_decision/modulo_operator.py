print("Please enter a whole number")
number = int(input())
#!= 0 means doesn't equal
if (number % 2 != 0):
  print("The number {} is odd".format(number))
else:
  print("The number {} is even".format(number))