def observed():
  observations = []
  for count in range(5):
    print("Please enter an observation:")
    observation = input()
    observations.append(observation)
  return observations

def remove_observations(observations):
  is_running = True
   
  while(is_running):
    removalquestion = input("Would you like to remove an observation? Yes/No ")
  
  if removalquestion == "Yes":
    whatobservation = input("Which observation would you like to remove?")
    observations.remove(whatobservation)
    print("Done! You have removed an observation")

  elif removalquestion == "No":
    print("Done!")

  else:
    print("You have inputted it wrong.")

  return observations

def run():
  observations = observed()
  remove_observations(observations)
  
  observations_set = set()
  
  for observation in observations:
    occurrences = observations.count(observation)
    observations_set.add((observation, occurrences))

  for key, value in sorted (observations_set):
    print(f"{key} observed {value} times")

run()


