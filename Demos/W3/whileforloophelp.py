#While loop 

While loops to print a countdown of number , from a user defined number

print("What is the starting point?")
start = int(input()) #control variable

while(start>=1): #condition which need to be satisfied for loop to continue
	print(start)
	start-=1 #modification to counter variable to avoid infinite loop
print ("BOOM!)



for counter in range(start, 0, -1)
	print(counter)
print ("BOOM!)