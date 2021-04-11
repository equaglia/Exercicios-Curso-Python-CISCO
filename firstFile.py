print("Hisssssss...")



#----------------

#hour = int(input("Starting time (hours): "))
#mins = int(input("Starting time (minutes): "))
#dura = int(input("Event duration (minutes): "))

# put your code here
#print("Expected output: "+str(((hour+(mins+dura)//60))%24)+":"+str((mins+dura)%60))

#-----------------------

#n =input("Sample input:")
#print("Expected output:",int(n) >= 100)

#-----------------------

# a = input("Sample input: ")

# if (a =="1"): 
#     a="Spathiphyllum"
# elif a =="2": 
#     a="spathiphyllum"

# if (a == "Spathiphyllum"):
#     answer="Yes - Spathiphyllum is the best plant ever!"
# elif (a == "spathiphyllum"):
#     answer="No, I want a big Spathiphyllum!"
# else: answer = "Spathiphyllum! Not "+a
# print(answer)

#-----------------------

#income = float(input("Enter the annual income: "))

# #
# # Put your code here.
# #
# if (income <= 85528):
#     tax = max(0, income*0.18 - 556.02)
# else:
#     tax = 14839.02+ (income-85528)*0.32

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

#-----------------------
#for i in range(1, 6):
# #while True:
# for x in range(5):
#     year = int(input("Enter a year: "))

#     #
#     # Put your code here.
#     #
#     if year >= 1582:
#         if year%4 != 0: yearType = "Common year"
#         elif year%100 != 0: yearType = "Leap year"
#         elif year%400 != 0: yearType = "Common year"
#         else: yearType = "Leap year"
#     else:
#         yearType = "Not within the Gregorian calendar period"

#     print(yearType)


#-----------------------

# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# a = secret_number -1
# while a!=secret_number:
#     a=int(input("So, what is the secret number?"))
#     if a!=secret_number: print("Ha ha! You're stuck in my loop!")
# print("Well done, muggle! You are free now.")
#-----------------------

# import time

# # Write a for loop that counts to five.
#     # Body of the loop - print the loop iteration number and the word "Mississippi".
#     # Body of the loop - use: time.sleep(1)
# for i in range(1,6):
#     print(i,"Mississippi")
#     time.sleep(1)


# # Write a print function with the final message.

#-----------------------

# # break - example

# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")


# # continue - example

# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")

# #-----------------------
# largestNumber = -99999999
# counter = 0

# number = int(input("Enter a number or type -1 to end program: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largestNumber:
#         largestNumber = number
#     number = int(input("Enter a number or type -1 to end program: "))

# if counter:
#     print("The largest number is", largestNumber)
# else:
#     print("You haven't entered any number.")
# #-----------------------
# largestNumber = -99999999
# counter = 0

# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largestNumber:
#         largestNumber = number

# if counter != 0:
#     print("The largest number is", largestNumber)
# else:
#     print("You haven't entered any number.")
#-----------------------

#while True:
#    a = input("Enter a word: ")
#    if a == "chupacabra":
#        break
#print("You've successfully left the loop.")
    
#-----------------------

# Prompt the user to enter a word
# # and assign it to the userWord variable.
# userWord = input("Enter a word: ")
# userWord = userWord.upper()
# wordWithoutVovels = ""
# for letter in userWord:
#     # Complete the body of the for loop.
#     if letter == "A": continue
#     elif letter == "E": continue
#     elif letter == "I": continue
#     elif letter == "O": continue
#     elif letter == "U": continue
#     wordWithoutVovels+=letter 
    
# print(wordWithoutVovels)
    
    
#-----------------------
# while True:
#     blocks = int(input("Enter the number of blocks: "))

#     #
#     # Write your code here.
#     #	
#     height = int((-1+(1+8*blocks)**0.5)/2)

#     print("The height of the pyramid:", height)

#-----------------------

# while True:
#     c0 = int(input("Number c0 = "))
#     steps = 0
#     if c0 <= 0:
#         print("Number must be an integer bigger than zero")
#         continue
#     while c0 != 1:
#         if c0%2 == 0: c0 = c0/2
#         else: c0 = 3*c0+1
#         print(int(c0))
#         steps+=1
#     print("steps = ",steps)

#-----------------------

# hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
# hatList[int((len(hatList)/2))] = int(input("Enter an integer = "))

# # Step 2: write a line of code here that removes the last element from the list.
# del(hatList[len(hatList)-1])
# # Step 3: write a line of code here that prints the length of the existing list.
# print(len(hatList))
# print(hatList)

#-----------------------

# # step 1
# beatles = []
# print("Step 1:", beatles)

# # step 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)

# # step 3
# for i in ["Sutcliffe", "Pete Best"]:
#     beatles.append(i)
# print("Step 3:", beatles)

# # step 4
# del(beatles[3])
# del(beatles[3])
# print("Step 4:", beatles)

# # step 5
# beatles.insert(0,"Ringo Starr")
# print("Step 5:", beatles)


# # testing list legth
# print("The Fab", len(beatles))
#-----------------------

# myList = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))

# for i in range(num):
#     val = float(input("Enter a list element: "))
#     myList.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(myList) - 1):
#         if myList[i] > myList[i + 1]:
#             swapped = True
#             myList[i], myList[i + 1] = myList[i + 1], myList[i]

# print("\nSorted:")
# print(myList)
#-----------------------

# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0

# for number in bets:
#     if number in drawn:
#         hits += 1

# print(hits)
#-----------------------

# myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# # put your code here
# #
# aux = []
# for number in myList:
#     if number not in aux:
#         aux.append(number)
# myList = aux

# print("The list with unique elements only:")
# print(myList)

#-----------------------

#squares = [x ** 2 for x in range(10)]
#print(squares)
#odds = [x for x in squares if x % 2 != 0 ]
#print(odds)
#-----------------------

# EMPTY = "-"
# ROOK = "ROOK"
# KNIGHT = "KNIGHT"
# PAWN = "PAWN"
# board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK

# board[4][2] = KNIGHT
# board[3][4] = PAWN

# print(board)

#-----------------------

# print("Average temperature at noon:", average)
# #print(temps[10])
# #print(temps[11])
# #print(temps[12])

# highest = -100.0

# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp

# print("The highest temperature was:", highest)

# hotDays = 0

# for day in temps:
#     if day[11] > 20.0:
#         hotDays += 1

# print(hotDays, "days were hot.")
#-----------------------
'''
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False

vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1
'''
#-----------------------
'''
# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0]) # outputs: ':('
print(table[0][3]) # outputs: ':)'

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0]) # outputs: ':('
print(cube[2][2][0]) # outputs: ':)'
'''
#-----------------------
'''
for i in range(-1, 1):
    print("#")

# printing range from negative to positive
for num in range(-2, 5):
    print(num, end=", ")

l = [0 for i in range(1,3)]
print(l)
'''
#-----------------------
"""
uma_lista = [3, 67, "gato", [56, 57, "cachorro"], [ ], 3.14, False]
print(uma_lista[2].upper())
print(uma_lista[2][0])


a = ['um', 'dois', 'três']
del a[1]
print(a)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista[1:5]
print(lista)


a = "banana"
b = "banana"
print('id a = ',id(a))
print('id b = ',id(b))
print(a is b)


a = [81, 82, 83]
b = [81, 82, 83]
print('id a ',id(a))
print('id b = ',id(b))
print('id a[0] ',id(a[0]))
print('id b[0] = ',id(b[0]))

print(a == b)
print(a is b)
print(id(b[0])-id(a[0]))
"""
#-----------------------
"""
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
"""

#-----------------------
'''
def isYearLeap(year):
    if year >= 1582:
        if year%4 != 0: return False
        elif year%100 != 0: return True
        elif year%400 != 0: return False
        else: return True
     #else: return None
         

#
# put your code here
#

testData = [1900, 2000, 2016, 1987,1000]
testResults = [False, True, True, False,None]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
'''
#-----------------------
def testIfInt(value):
    if type(value) == int:
        return True

def isYearLeap(year):
    if type(year) != int:
        return None
    if year >= 1582:
        if year%4 != 0: return False
        elif year%100 != 0: return True
        elif year%400 != 0: return False
        else: return True
     #return None
#
# your code from LAB 4.1.3.6
#

def daysInMonth(year, month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    yrLeap = isYearLeap(year)
    if type(month) != int or yrLeap == None:
        return None
    if yrLeap and month == 2:
        return 29
    if month >= 1 and month <= 12:
        return months[month-1]
    #return None
    
#
# put your new code here
#
'''
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
'''
#-----------------------

#def isYearLeap(year):
#
# your code from LAB 4.1.3.6
#

#def daysInMonth(year, month):
#
# your code from LAB 4.1.3.7
#

def dayOfYear(year, month, day):
    daysMonth = daysInMonth(year, month)
    if type(day) != int:
        return None
    if daysMonth != None:
        if daysMonth >= day and day > 0:
            return str(day) + "/" + str(month) + "/" + str(year)
    

#
# put your new code here
#

print(dayOfYear(2000, 12, 31))

testYears = [1900, 2000, 2016, 1987, 1900, 2000, 2016, 1987, 1000, 1900, 2000, 2016, 1987, 1000, 2020, 2022, "d"]
testMonths = [2, 2, 1, 11, 2, 2, 1, 11, 1, 2, 3, 4, 5, 16, "b", 8, 2]
testDays = [28, 29, 31, 30, 27, 27, 27, 27, 30, 30, 30, 30, 32, 10, 15, "c", 23]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	da = testDays[i]
	print(str(da)+"/"+str(mo)+"/"+str(yr)+" = ",end="")
	print(dayOfYear(yr, mo, da))
	'''
	print(yr, mo, da, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
		'''

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
#-----------------------
#-----------------------


