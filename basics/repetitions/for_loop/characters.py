print( "What strange character do you see?") #asking user 
characters=input() #user input
print("\nIdentyfing...\n")

for symbol in range(0,len(characters),1): #string indexing parameters
  
  print("index ",symbol ,":", characters[symbol] )
