print("Towards which direction should I paint (up, down, left or right)")
paint = str(input())

if (paint == "up"):
  print("I am painting upwards")
elif (paint == "down"):
  print("I am painting downwards")
elif (paint == "right"):
  print("I am painting to the right")
elif (paint == "left"):
  print("I am painting to the left")

else:
  print("Please choose a direction")