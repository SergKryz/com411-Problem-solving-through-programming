def display_ladder(steps):
  for step in range (steps):
    print("| |\n***")
  
  print("| |")#bootom of a ladder


def create_ladder():
  print("How many steps remain?")
  steps=int(input())
  display_ladder(steps)

create_ladder()