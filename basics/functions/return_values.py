def sum_weights(beepw,bopw):
  total=beepw + bopw
  print(total)
  return total
  

def calc_avg_weight(beepw,bopw):
  average =(beepw+bopw )/ 2
  return average
  

def run():
  print("Enter beeps  weight:")
  beepw=float(input())\
  print("Enter bops weight:")
  bopw=float(input())

  print("What would you like to calculate? (sum/average)") 
  action=input()

  if (action=="sum"):
    answer = sum_weights(beepw,bopw)
    print(" The sum of their weight is {:.2f} " .format(answer))
  elif(action=="average") :
    answer = calc_avg_weight(beepw,bopw) 
    print("The average of their weight is {:.2f}" . format(answer))

  else:
    print("I am not sure what you would like to do.")

run()