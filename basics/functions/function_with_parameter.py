def escape_by(plan):#defining function with one parameter

  if (plan=="jumping over"):#setting conditions
    print("We cannot escape that way. The boulder is too big!")

  elif(plan == "running around")  :
    print ("We cannot escape that way! The boulder moving too fast!")

  elif ( plan =="going deeper"):
    print("It might help - let's gor deeper!!!")

  else:
    print("\nWe can not escape that way. Boulder blocking it!")


escape_by("jumping over")#calling up for functions
escape_by("running around")
escape_by("going deeper") 


escape_by("anything else")