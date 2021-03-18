

print("Program started !") # Welcome message of the program
 
print("Please enter a standard character:")# Asking user for input

x= input()


if  (len(x) == 1): # program coditions
  print(f"The ASCII code for {x} is {ord(x)}.")

else:
  print("ERROR! Please check is  the character a single symbol!")


print("Program ended!")




