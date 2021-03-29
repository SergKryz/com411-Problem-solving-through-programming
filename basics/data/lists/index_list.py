def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  lista = movements()
  print(f"{lista[0]} for {lista[1] } steps")
  print(f"{lista[2]} for { lista[3] }steps")
  print(f"{lista[4]} for {lista[5]} steps")
  print(f"{lista[6]} for {lista[7]} steps" )

run()

