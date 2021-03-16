#define a list

fruits = []

#Define list with items

vegetables = ["Carrot", "Peas"]
#print(vegetables)

#Add items to the list

fruits.append("Apple")
fruits.append("Bannana")#append adds to the end of the list
fruits.append("Tomatoe")
fruits.append ("Bannana")


print(fruits)

#remove an item from a list
#method -function which belongs to an item/list.

fruits.remove("Bannana")
print(fruits)

#Remove item by index

del fruits[1]
print(fruits)

#Insert a value not at the end (that what add does)

fruits.insert(1, "Pineapple")

print(fruits)


#Access single element
print(fruits[0]) #prints item by index in the list

#https://docs.python.org/3/tutorial/datastructures.html