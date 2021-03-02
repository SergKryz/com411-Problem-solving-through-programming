print ("What is your name?")
n = input()
print(" Do you have a dog? (types tru or false)")
dog = bool(input())
#boolean is datatype - only true or false

if len(n) > 9 and dog:
  print ("You have very long name!")
  print ("Your name contains {} letters". format(len(n)) )
else:
  print("Your name is alright.")  
print("This is the end of a program")  