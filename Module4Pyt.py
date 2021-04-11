print("Hisssssss...")

'''
#-----------------------
# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.
mile = 1609.344
gallon = 3.785411784
cemMil = 100000

def l100kmtompg(liters):
    gls = liters/gallon
    mls = cemMil/mile
    return mls/gls

#
# put your code here
#

def mpgtol100km(miles):
    kms = miles/cemMil
    lts = gallon/mile
    return lts/kms
    
#
# put your code here
#

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
'''
#-----------------------
'''
def soma_n(*args):
    acc = 0
    for arg in args:
        acc += arg
    return acc

print(soma_n(5,6,7,8,9,10))
'''
#-----------------------
'''
def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c): # Right Triangle
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2


def heron(a, b, c): # Heron Field
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def fieldOfTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return None
    return heron(a, b, c)

print(fieldOfTriangle(1., 1., 2. ** .5))

print(isItRightTriangle(5, 3, 4))
print(isItRightTriangle(1, 3, 4))
print(isItRightTriangle(3, 5, 4))
'''
#-----------------------
"""
def factorialFun(n): # Factorial
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

# Recursive implementation of the factorial function
def factorial(n):
    if n == 1:    # the base case (termination condition)
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24
for n in range(1, 10): # testing
    print(n, factorial(n))
"""    
#-----------------------
"""
def fib(n): # Fibonacci
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum
"""
'''
def fib(n): # Fibonacci with Recursion
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, 10): # testing
    print(n, "->", fib(n))
'''
#-----------------------
"""
dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['cat'])
print(phone_numbers['Suzy'])

#print(phone_numbers['president'])

print()

#dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

print()
for key in dictionary.keys():
    print(key, "->", dictionary[key])
print()
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
print()
for english, french in dictionary.items():
    print(english, "->", french)
print()
for french in dictionary.values():
    print(french)
print()
myTuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print("myTuple = ",myTuple)

myList = [1, 2, True, "a string", (3, 4), [5, 6], None]
print("myList = ",myList)
"""
#-----------------------
"""
def func(a, b):
    return a**a
print(func(2))

# 1, 5, 17
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

def fun(x, y, z):
    return x + 2 * y + 3 * z
print(fun(0, z=1, y=3))

def fun(x):
    x += 1
    return x

x = 2
x = fun(x + 1)
print(x)

def any():
    print(var + 1, end='')
var = 1
any()
print(var)

def func1(a):
    return a ** a
def func2(a):
    return func1(a) * func1(a)
print(func2(2))

def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)

def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(3))

tuple = ("alpha","bravo","charlie")
print (tuple)
tuple[1] = tuple[1] + tuple[0]


def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))

dct = { 'one':'two', 'three':'one', 'two':'three' }
v = dct['one']
for k in range(len(dct)):
    v = dct[v]
    print(v)
print(v)

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(fun(fun(2)) + 1)

dct = { }
lst = ['a', 'b', 'c', 'd']
for i in range(len(lst) -1):
    dct[lst[i]] = ( lst[i], )
for i in sorted(dct.keys()):
    k = dct[i]
    print(k[0])

"""
list = ['Mary', 'had', 'a', 'little', 'lamb']
def list(lst):
    del lst[3]
    lst[3] = 'ram'
print(list(list))
#-----------------------
#-----------------------
#-----------------------
#-----------------------


