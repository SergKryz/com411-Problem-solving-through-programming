
#len() is a built-in function in python.You can use the len() to get the length of the given string, array, list, tuple, dictionary, etc.
##Value: the given value you want the length of.
#Return value a return an integer value i.e. the length of the given string, or array, or list, or collections.
print("Please enter a phrase")



phrase=input()

bops=0 # Declare a control variable

while(bops< len(phrase)):
  print ("Bop", end =" ")
  bops+=1
print("\n END ")