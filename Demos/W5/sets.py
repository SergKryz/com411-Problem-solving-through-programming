#creating a set


colours =set()
print(type(colours))


#initialise non-empty set

colors ={ "blue", "red", "yellow"}
print(type(colors))
#print(colors)

#adding elements to set

colors.add("purple")
colours.add(" red")

# print(colours)
# print(colors)#

colours.add("black" )
colours.add("green" )

print(colours)
print(colors)

#Union joining two sorted

set1= colours.union(colors)
print(set1)


#Intersection - finding common elements

set2 = colors.intersection(colours)
print(set2)