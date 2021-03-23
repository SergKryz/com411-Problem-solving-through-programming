def box(word):
  num_dashes = 4 + len(word)
  print("-" * num_dashes)
  print("| {} |".format(word))
  print("-" * num_dashes)


def lower_case(word):
  print(word.lower())

def upper_case (word):
  print(word.upper())

def mirrored(word):
  mirrored = " "
  for letter in reversed(word):
   mirrored += letter
  print("{} | {} " . format(word, mirrored))

def repeat(word):
  print("How many times display word?")
  
  times = int(input())

  for repetition in range(times):
    if (times % 2 == 0):
      print(lower_case(word))
    else:
      print(upper_case(word))
 

def run():
  print("Please type the word:")
  word=input()

  response = 0
  while (response != 6):
        # get the user's selection
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input()) 
 
        # determine and execute action
        if (response == 1):
           box(word)
        elif (response == 2):
          lower_case(word)
        elif (response == 3):
          upper_case(word)
        elif (response == 4):
            mirrored(word)
        elif (response == 5):
          repeat(word)
        elif (response == 6):
            
            print("END OF THE PROGRAM.")
        else:
            print("Unknown option.") 


run()

