#bot.py
print("Enter the whole number.")

number=int(input())

if (number%2==1) : #using modulo operator to find a number type
  print("The number {} is an odd number." .format(number))
else:
  print("The number {} is an even number." .format(number))

print("END OF THE PROGRAM.")