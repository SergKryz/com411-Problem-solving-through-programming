

#https://www.abc.net.au/news/science/2018-01-20/how-prime-numbers-rsa-encryption-works/9338876#:~:text=The%20reason%20prime%20numbers%20are,17%2C%20or%20187%20and%201.

#Finding is the number prime

def isPrime(x):
	for i in range (2,x):
		if x%i== 0:
		  return False
		return True

#Finding prime nr


def findPrime(begin, finish):

	for j in range(begin, finish):
	  if isPrime(j):
 	    return j



#encrypt gives instructions under function and will 
#find another function in code

def encrypt():
	
	print("provide two integers")
	x=int(input())
	y=int(input())
	prime1 = findPrime(x,y)
	print ("provide two more integers.")
	x=int(input())
	y=int(input())
	prime2 = findPrime(x,y)
	return prime1*prime2


print(encrypt())










#Finding prime nr

# 
# def findPrime(begin, finish):

# 	for j in range(begin, finish):
# 	  if isPrime(j):
#  	    return j
# 

# x=15
# y=28

# print(f"The prime between {x} and {y} is {findPrime(x,y)}. ")






# ''' print ("Whats is the number?")

# x=int(input())
# if isPrime(x):

# print(f"The number {x} is prime!")
# else:
#   print("The number is not prime!")
# '''


