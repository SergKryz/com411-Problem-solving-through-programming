def likelihood():
  likelihood=(50,38,27,99,4)
  return (min(likelihood), max(likelihood))

def run():
  minimumtemp=likelihood()


  print(f"Minimum likelihood of falling: {minimumtemp[0]} %")
  print(f"Maximum likelihood of falling: {minimumtemp[1]} %")


run()