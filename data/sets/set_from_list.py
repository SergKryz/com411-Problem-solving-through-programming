def observed():
  observations=[ ]
  for n in range(7):
    print("What did you see?")
    seen=input()
    observations.append(seen)
  return observations
  

def run():
  print("Counting observations...")
  lista=observed()
 # populate set
  lista1=set()
  count=0
  for see in lista:
    if count <len(lista) :
       lista2=(lista[count], lista.count(see))
       count+=1
     
    lista1.add(lista2)
   # display set    
  for lista2 in lista1:     
    print(f"{lista2[0]} observed {lista2[1]} times")
    
  

run()
