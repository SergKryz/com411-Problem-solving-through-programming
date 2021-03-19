def getmefruits(): 
  fruits=[]
  print("How many fruits would you like to enter?")
  n = int(input())
  for i in range(n): #starts at 0 by default, 4 is excluded
	  print("Type in the next fruit:")
	  fruits.append(input())
  return fruits

  

 

def get_fruits():
	fruits =["apple ", "kiwi", "bannana", "mango", "pineapple", "pear"]
	fruits2= getmefruits()    


	print("Your fruits are {}" .format(fruits))
	print("Your fruits are {}" .format(fruits))


	print(f"Sliced list: {fruits[0:2]}") #could be [0:5:2] from 0 to 5 (excluded) in steps of 2
	
'''
	
#print only few items 
print(f"Negative index: {fruits[-2:0:-1]}")

get_fruits() #calling function


person = ("Piotr", 67 , False)

print(person)

print(person[1])


if person[2]:
	print ("Yay - you have a doggo!")
else:
	print("No doggo no fun!")


print("Which item to print?")
n= int(input())
if n< len(person)
	print(person[n-1])
#you can not modify(mutate) a tuple !
#person[0] = "Peter"
#print(person)

print(person +2000, "black")






#

def student() :
	print("Enter your name?")
	name = input()
	print(" What is you age? ")
	age = int(input())
	print("Do you have a dog? ")
	dog =  input()
	if dog=="yes":
		dog_bool = True
	else:
		dog_bool = False
	return name,age, dog_bool

print(student())

print ("How many students to generate? ")

n = int(input())
count= 0
all_students = []
while(count < n):
	tuplex = student()
	all_students.append(tuplex)
	count+=1
print (all_students)

'''

get_fruits()

