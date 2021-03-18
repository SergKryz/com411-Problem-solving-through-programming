

print("Program started !") #program begins

print("Please enter the ASCII code:") # Asking for user input

x= int(input())

if (x>=32 and x <126): # program conditions
  print (f"The character represented by the ASCII code {x} is { chr(x) }." )

else:
  print(" Number {} is within specified range (32-126)!" .format (x))

print("End of the program.")