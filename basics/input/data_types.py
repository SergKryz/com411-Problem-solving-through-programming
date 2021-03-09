print("What is your name?")
name = str(input())

print("How old are you?")
years = int(input())

print("How tall are you (in meteres) ?")
height = float(input())

print("What is your wheight in kilograms?")
weight = int(input())

x = weight/height**2

print("{} you are {} and your bmi is {:.0f} ." .format(name,years,x))


