print("Hisssssss...")
'''
import math
for name in dir(math):
    print(name, end="\t")
    '''
#-----------------------
'''
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print(platform())
print(platform(1))
print(platform(0,1))

print(machine())
print(processor())
print(system())
print(version())

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
    '''
#-----------------------
'''
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
'''
'''
if secondNumber != 0:
    print(firstNumber / secondNumber)
else:
    print("This operation cannot be done.")
'''
'''
try:
    print(firstNumber / secondNumber)
except:
    print("This operation cannot be done.")

print("THE END.")
'''
#-----------------------
'''
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
'''
#-----------------------
'''
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# we must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
'''
#-----------------------
'''
# the code shows an extravagant way
# of leaving the loop

list = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False

print('Done')
'''
#-----------------------
'''
# this code cannot be terminated
# by pressing Ctrl-C

from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")
'''        
#-----------------------
'''
# the code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')
'''
#-----------------------
'''
# how to abuse the dictionary
# and how to deal with it

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)
'''    
#-----------------------
'''
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# we must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
'''
#-----------------------
'''
def readint(prompt, min, max):
    while True:
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range (-10..10)")
        

v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
'''
#-----------------------

def mysplit(strng):
    strlist = list(strng)
    endlist = []
    listitem = ""
    for elem in strlist:
        if elem == " ":
            if listitem != "": endlist.append(listitem)
            listitem = ""
            elem = ""
        else:
            listitem+=elem
    if listitem != "": endlist.append(listitem)
    return endlist
#
# put your code here
#

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
#['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
#[]
#['abc']
#[]

#-----------------------
# Demonstrating the list() function
#print(list("abcabc"))

# Demonstrating the count() method
#print("abcabc".count("b"))
#print('abcabc'.count("d"))
#-----------------------


#-----------------------


#-----------------------
#-----------------------


#-----------------------
#-----------------------


#-----------------------



