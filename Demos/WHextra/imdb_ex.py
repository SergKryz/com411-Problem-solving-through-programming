def actors():
  real=input("Name:")
  role=input("Role:")
  return real, role #returning tuple(,), returning list[]

def rate_movie(title):
  return float(input(f"What would you rate \"{title}\"?\n"))

def new_movie():
    #function to create movie page
    movie={}  # creating dictionary
    movie["Title"]= input("What is the movie title?\n")
    # movie["Released"]=input("What year was it released? \n")
    movie["Genre"]=input("What genre it is?\n")
    # movie["Duration"]=input("Movie length?\n")
    actor_list = []
    i=0
    print("Provide details of the cast. How many actors are in the cast?")
    n=int(input())
    while i < n:
      
      actor_list.append(actors())
      i+=1
    movie["Actors"]=actor_list
    movie["Rating"]=5.0,0
    return movie

def movie_search(database={}):
  print("Searh by: Title, Genre or Actor?")
  opt=input()
  movie={}
  if opt.lower() == "title":
    t = input("Enter the title:")
    if t in database:
      movie = database[t]
    else:
      print("No info in database. ")
  elif opt.lower()== "genre":
    g=input("Enter the  genre:")
    for details in database.values():
      if details["Genre"] == g:
        movie= details
  elif opt.lower() == "actor":
    a = input ("Enter actor's name:")
    for details in database.values():
      for actor in details["Actors"]:
        if actor[0]== a:
          movie=details

def max_rated(database= {}):
  max_rating=0
  for details in database.values():
    if details["Rating"][0]>max_rating:
      max_rating = details["Rating"][0]
      movie=details
  return movie


def movie_print(movie ={}):
  print("*"*10 + " "*2 + "{}".format(movie["Title"]) + " "*2 + "*"*10)
  for item in movie.items:
    print(f"{item[0]}--------------> {item[1]}")





def imdb():
  imdb={}
  print("Welcome to IMDB !\n\n")
  while True:
    print("Choose an item from the menu:\n1-Add a movie\n2-Search for a movie\n3-Display all movies\n4-Top rated movies\n5-Add a rating\n9-Exit")
    option=int(input())
    if option==1:
      m_title = input("What is the title of the movie?")
      imdb[m_title]= new_movie()
    elif option == 2:
      print(f"Suitable movie:{movie_print(movie_search(imdb))}")
    elif option == 3:
     print(imdb)
    elif option == 4:
     print("Highest rated movie:")
     print(max_rated(imdb()))
    elif option == 5:
      print("You are rating a movie. ")
      m=movie_search(imdb)
      current_rating =m["Rating"][0]
      number_rating = m["Rating"][1]
      x=rate_movie(m["Title"])
      new_rating= (number_rating*current_rating + x)/(number_rating + 1)
      m["Rating"]=new_rating,number_rating + 1
      imdb[m["Title"]]= m
    elif option == 9:
      break
    else:
      print("Invalid option.")
  return imdb



imdb()