print( "What phrase do you see?") #asking user 

phrase=input() #Inputing user Inputing

print("\nReversing...\nThe phrase is: ", end="") 

for reverse in range(len(phrase)-1,-1,-1): #

  print( phrase[reverse], end="" )