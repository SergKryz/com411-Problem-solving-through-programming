print(" What type book cover you would like to have? (soft/hard)")
book=input()

if (book=="soft"):
  print(" If the cover is perfect bound?(yes/no)")
  bound=input()

  if (bound=="yes"): 
      print("Soft cover, perfect bound books are very popular!")

  else:
      print("Soft covers with coils or stitches are great for short books.")  
else:
  print("Books with hard covers can be more expensive!")   


print("END OF THE PROGRAM.")    