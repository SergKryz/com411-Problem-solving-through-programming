def likelihood():
  likelihood=(50,38,27,99,4)
  return min(likelihood)

def run():
  minimumtemp=likelihood()

  print(f"Minimum likelihood of falling: {minimumtemp} %")

run()