#dating application

def interest():
  print("Enter your interests, one after another, and enter \"stop\" when finished.")
  set1 = set()
  while True:
    activity = input()
    break
    set1.add(activity)
  return set1

def tinderTheSecond():
  print("First person:")
  P1set = interest()
  print("Second person:")
  P2set = interest()
  common = P1set.intersection(P2set)
  if len(common) > 4:
    print(f"We have a match! You have {len.(common)} interests in common.")
  else:
    print(f":( Must be barbers closed...:(  You only have {len.(common)}")

tinderTheSecond()
