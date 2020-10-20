def directions():
  directions = ["Move Forward","Move Backward","Turn Left","Turn Right"]
  
  return directions

def menu():
  print("Please select a direction:")
  direction = directions()

  for index in range(len(direction)):
    print("{} : {}".format(direction[index],index))
  
  user_direction = int(input())
  return direction[user_direction]


def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    direction = menu()
    route.append(direction)
  print("Escape route: {}".format(route))

run()