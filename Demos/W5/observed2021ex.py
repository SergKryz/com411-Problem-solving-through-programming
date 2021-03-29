
def observed():
   observations=[]
   for i in range(7):
     observations.append(input())
   return observations


def run():
  print("Counting observations...")
  list_of_obs = observed()
  set_of_obs = set() 
  for i in range (len(list_of_obs)):
    set_of_obs.add(list_of_obs[i])
  set_of_tuples = set()
  for item in set_of_obs:
    count=0
    for i in range (len(list_of_obs)): 
      if list_of_obs[i]==item:
        count +=1
    set_of_tuples.add((item, count))
  print(set_of_tuples)

run()
