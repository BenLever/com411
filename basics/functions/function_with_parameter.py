def escape_by(plan):
  if (plan == "jumping over"):
    print("We cannot escape that way! The boulder is too big!")
  elif (plan == "running around"):
    print("We cannot escape that way! The boulder is moving too fast!")
  elif (plan == "going deeper"):
    print("That might work! Let's go deeper")
  else:
    print("We cannot escape that way! The boulder is in the way!")

plan = input()
escape_by(plan)