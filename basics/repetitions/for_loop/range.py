print( "What level of brightness is required?") #asking user 
bright=int(input()) #taking user input
print("\nAdjusting brightness...\n")

for count in range (2,bright+1,2): # Loop condition(+1 is needed to show last digit as its excluded )

  print("Brightness level:", "\u2600 " * count ) # printing result