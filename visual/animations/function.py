#matplotlib funcanimation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
        
def animate(frame):
  print(f"{frame} - frame number")


def run():

  fig, ax = plt.subplots()
  
  some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  plt.show()

run()