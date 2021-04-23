import csv,random

def save_pokes(pokes = []): # work on save.txt File
  with open("pokemon.txt", "w") as sv: # as gives file a name
    for pokemon in  pokes:
      sv.write(pokemon + "\n")

def save_pokes_csv(pokes = []): #have to ipmort csv modue in begining of the script
  with open("pokemon.csv","w") as sv:
    data_writer = csv.writer(sv, delimiter=",", quotechar='"' ) #in order to write in csv file we need to create this thing with parameters/instructions
    data_writer.writerow(pokes) #calling writer

def load_pokemon():     #printing txt file on a panel (print(load_pokemon()))
  with open("pokemon.txt") as ld:
    return ld.read().split() #read turns shows it as a string # split creates as  a list

def load_pokemon_csv():
  with open("pokemon.csv") as ld:
    csv_reader = csv.reader(ld, quotechar = "'") # delimiter not specified, coma by default
    return list(csv_reader)[0] # calling first list as there is a list in a list


def random_poke(): #need to import random module in beginnig of the code , same as csv module
  with open("poke_database.csv") as pok:
    csv_reader = csv.reader(pok,quotechar="'" )
    new_poke = list(csv_reader)[random.randint(0,1046)]
    return new_poke[2]




def run():
  print("\033[92m Welcome Pokemon Trainer \033[0m")
  while True:
    print("\n What would you like to do?\n1.View My Pokemon\n2.Add New Pokemon\n3.Add a random Pokemon\n4.Exit")
    opt=int(input())

    if opt == 1:
      print(load_pokemon_csv())
    elif opt == 2 :
      new_poke=input("Enter the name: ")
      poke_list=load_pokemon_csv()
      poke_list.append(new_poke)
      save_pokes_csv(poke_list)
    elif opt ==3 :
      new_poke = random_poke()
      print(f"Well done! You have captured {new_poke}!")
      poke_list = load_pokemon_csv()
      poke_list.append(new_poke)
      save_pokes_csv(poke_list)
    elif opt==4:
      break


   

run()