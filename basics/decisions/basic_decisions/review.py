print("What would you like, human?")
something=input()


if (something=="paint") or (something=="play"):
  print("What is your favourite color?")
  color=input()
  if (color=="green") or (color=="blue") :
      print("I love to play with {} ball. " .format(color))
  else:
    print(" Lets play with {} ball ! ".format(color))    
else:
  print("Something else")
  
    

print("END OF THE PROGRAM.")
