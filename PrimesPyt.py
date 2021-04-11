print("Hisssssss...")

#-----------------------

def isPrime(num, primesList=None):
    last = 2
    if primesList == None: # Compare with all numbers
        for i in range(2, num-1):
            if num % i == 0:
                return False
        return True
    if len(primesList) > 0: # Compare only with the primes already found
        last = primesList[len(primesList)-1]
        for i in primesList:
            if num % i == 0:
                return False
    for i in range(last, num):
        if num % i == 0:
            return False
    return True


def isPrimeList(num):
    limit = int(num**(0.5))
    print(limit)
    list = []
    for i in range (2,num+1):
        list.append(i)
    for i in list[:limit]:
        #print("i = ",i)
        if i in list:
            for j in list[list.index(i)+1:]:
                if j % i == 0:
                    #print("removendo j = ",j)
                    list.remove(j)
    return list
#
# put your code here
#
import time

ini = time.time()
num = input("Enter number = ")
listOfPrimes = isPrimeList(int(num))
print(listOfPrimes)
print("Quantity of primes = ",len(listOfPrimes))
fim = time.time()
print ("Função isPrime(num, primesList): ", fim-ini)

print("""


""")

ini = time.time()
numOfPrimes = 0
primes = []
for i in range(1, int(num)):
	if isPrime(i + 1, primes):
			#print(i + 1, end=" ")
			primes.append(i+1)
			numOfPrimes +=1
print()
print("Quantity of primes = ",numOfPrimes)
#print("primes = ", primes)
fim = time.time()
print ("Função isPrime(num, primesList): ", fim-ini)
#-----------------------
#-----------------------
#-----------------------
#-----------------------
#-----------------------
#-----------------------
#-----------------------
#-----------------------
#-----------------------
#-----------------------

