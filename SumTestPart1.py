print("Hisssssss...")

#-----------------------
print("q1")
dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1],end="")
#-----------------------
print()
print("q2") # is erroneous - Falha 1/4
def func(a,b):
    return b ** a

#print(func(b=2, 2))
#-----------------------
print()
print("q3")
x = 1 // 5 + 1 / 5
print(x)
#-----------------------
print()
print("q4")
def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))
#-----------------------
print()
print("q5")
'''
y = input()
x = input()
print(x + y)
'''
#-----------------------
print()
print("q6")
'''
i = 0
while i < i + 2:
    i += 1
    print("*")
else:
    print("*")
    '''
#-----------------------
print()
print("q7")
lst = [1, 2]

for v in range(2):
    lst.insert(-1, lst[v])

print(lst)
#-----------------------
print()
print("q8") # [0, 1, 4, 9] - Falha 2/4
list = [x * x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(list))
#-----------------------
print()
print("q9")
1 // 2
print(1 // 2)
#-----------------------
print()
print("q10")
def func1(a):
    return None

def func2(a):
    return func1(a) * func1(a)

#print(func2(2))
#-----------------------
print()
print("q11")
print("a", "b", "c", sep="sep")
#-----------------------
print()
print("q12")
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
#-----------------------
print()
print("q13")
'''
dd = { "1":"0", "0":"1" }
for x in dd.vals():
    print(x, end="")
    '''
#-----------------------
print()
print("q14")
nums = [1, 2, 3]
vals = nums
del vals[:]
print("nums = ",nums)
print("vals = ",vals)
#-----------------------
print()
print("q15")

#-----------------------
print()
print("q16")
nums = [1, 2, 3]
vals = nums
#-----------------------
print()
print("q17")
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
#-----------------------
print()
print("q18")
tup = (1, 2, 4, 8)
print(tup)
tup = tup[-2:-1]
print(tup)
tup = tup[-1]
print(tup)
#-----------------------
print()
print("q19")

#-----------------------
print()
print("q20") # zero - Falha 3/4
lst = [i for i in range(-1, -2)]
print(len(lst))
print(lst)
#-----------------------
print()
print("q21")

#-----------------------
print()
print("q22")
'''
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
'''
#-----------------------
print()
print("q23")
'''
x = float(input())
y = float(input())
print(y ** (1 / x))
'''
#-----------------------
print()
print("q24")
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))
#-----------------------
print()
print("q25")
z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)
#-----------------------
print()
print("q26")
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
#-----------------------
print()
print("q27") # != - Falha 4/4
print(x != y)
#-----------------------
print()
print("q28")
def fun(x, y):
    if x == y:
        return x
    else:
        return fun (x, y-1)

print(fun(0, 3))
#-----------------------
print()
print("q29")
dct = { 'one':'two', 'three':'one', 'two':'three' }
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)
#-----------------------
print()
print("q30")

#-----------------------

