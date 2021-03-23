#program that imitates small database , which can :
#insert new students and a mark for their assigment
#keep continouly add students
#print out students name and a mark
#average mark of all students
#find the maximu marko among all

def generate_stds():
  print("Enter the name:")
  name = input()
  print("Enter the grade:")
  grade = int(input())
  return name, grade

#print(generate_stds())  

#t = generate_stds()
 # print(t)

def all_stds():
  all_students = []
  while True :
    all_students.append(generate_stds())
    print("To stop adding students press 0.")
    x = input()
    if x == '0':
      break  #quit loop
  return all_students

#print(all_stds())

def print_students(lista):
  for std in lista:
    print(f"{std[0]} earned a grade {std[1]}")

#print_students(all_stds())


def avg_mark(sarasas):
  total = 0
  for std in sarasas:
    total+=std[1]
  return total/len(sarasas)

print(avg_mark(all_stds()))