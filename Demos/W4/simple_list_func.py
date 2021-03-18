def get_fruits(): 
	fruits=[]
	print("How many fruits would you like to enter?")
	n = int(input())

	for i in range(n): #starts at 0 by default, 4 is excluded
	  print("Type in the next fruit:")
	  fruits.append(input())
	print("Your fruits are {}" .format(fruits))

#accessing only several items of the list(slicing)
	print(f"Sliced list: {fruits[0:2]}") #could be [0:5:2] from 0 to 5 (excluded) in steps of 2

#print only few items 
print(f"Negative index: {fruits[-2:0:-1]}")

get_fruits() #calling function