
print("How many numbers should I sum up?")

number=int(input()) #asking user for a number

kint=1  #controlling variable
print() #Wondering why this new line for ???

total=0

while (kint<=number): #condition
  
 
  
  print("Please enter number {} of {}:" .format(kint, number))
  anynumber=int(input())
  kint=kint +1
  total=total+anynumber
  



print ("The answer is ", total) #printing answer - sum of number entered
