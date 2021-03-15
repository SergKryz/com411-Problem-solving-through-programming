print("How many live cables must I avoid?")

cablestoavoid=int(input())

livecables=0

while(livecables<cablestoavoid):
  print(" Avoiding ...", end="")
  print("Done...{} live cable avoided!" .format(cablestoavoid))
  cablestoavoid-=5

print( "All live cables have been avoided.")  