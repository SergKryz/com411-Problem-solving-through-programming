# dict1={}

# dict2={"name": "Piotr", "age":26 , "alergy": ["coffee" , "hard working"]}



# dict2["siblings"]=2 #Adding to dictionary new value

# for item in dict2:
#   print(item)

# #print(dict2["name"])


phonebook = {}

while True:
  name = input("Enter the name: ")
  number= input("Enter the number: ")
  phonebook[name] = number
  if input("Type 'x' to stop!") == "x":
    break

#print(phonebook)

def calling(n,book= {}):
  print(f"Calling {n} with aphone number {book[n]}")


calling("Piotr", phonebook)