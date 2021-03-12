"""

# importing files in main.py
#import roomcalc ( imports the file)
#roomcalc.run - runs the code

#from roomcalc import run  (specifies what to import , single or more functions)
---------------------------------------------------------------------------------
another way of importing

import roomcalc.run as runningthis

runningthihs()

------------------------------------------------------

#importing from folder

import Demos.W3.roomcalc as room 

room.run()

#importing from demos folder, then accesses other folder inside
main folde and opens file specified (roomcalc as) name roomc and runs that functions
--------------------------------------------------------

#example

import Demos.W3.roomcalc as room 

print(room.price("bathroom", 10))

"""