
import random

print("Please enter the minimum value:")
minv= int(input())
print("Please enter the maximum value:")
maxv= int(input())

rannumber = random.randrange(minv,maxv) 
print(rannumber)

print(f"I am thinking of number between {minv} and {maxv} ?")



guessed=0

while guessed != rannumber:
  print("Guess the number:")

  guessed= int(input())

  if guessed < rannumber:
    print("Your guess is too low")
    print("Try again:")
  elif guessed > rannumber:
    print("Your guess is too high") 
    print("Try again:")
  else:
    print("Congrats, you guessed it! ")
    print("End of the program")
    break