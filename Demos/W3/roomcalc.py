#Code that can be used to calculate the total cost of room makeover in a house

def room_area( width,length) :#1
	return width*length

def room_name():#2
	print("What is the name of the room?")
	return input() #return basically saves a value in memory

def price(name, area) :# DEF 1 AND 2
	if name == "bathroom":
	  return 20*area
	elif name =="kitchen" :
	  return 10*area
	else:
	  return 7*area

def run(): #Main code
	name = room_name()
	print("What is the width of the room?")
	w = float(input())
	print("What is the length of the room?")
	l = float(input())
	print(f"You should pay £ {price(name,room_area(w,l))}")  #f - formatting 


run() #executes all the code above