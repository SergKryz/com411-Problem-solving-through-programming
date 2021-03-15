print("How many bars should be charged?")
barstoc=int(input()) #How many bars to charge input by user

bars_charged=0 #created variable to count bars charged

while(bars_charged<barstoc): #condition

  bars_charged = bars_charged + 1 # same thing as bars_charged += 1


  print("Charging:" , "\u26a1" * bars_charged)
  
  


print  ("The battery is fully charged.")
