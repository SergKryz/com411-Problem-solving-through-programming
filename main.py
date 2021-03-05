# #We wish to create a program that allows us to specify what type of book is 
# being read by Beep.
# The program should start by asking the user to enter the type of book e.g. 
# adventure.
# If the book is an "adventure" book then the message "I like adventure 
# books!" should be displayed.
# Finally, the program should display "Finished reading book!" .

print("Choose book category: \n\n1-Fantasy\n2-Adventures\n3-Comedy")

option = int(input())

if option == 1:
  print("Fantasy books are great.")
elif option == 2:
  print("I like adventure.")  
elif option ==3:
  print("Comedy books are so funny. ")
else:  
  print("There is no such a option!")

print("Finished reading book!")  