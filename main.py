print( "What strange character do you see?") #asking user 
characters=input()
print("\nIdentyfing...\n")

for symbol in range(0,len(characters),1): 
  print("index ",symbol ,":", characters[symbol] )

