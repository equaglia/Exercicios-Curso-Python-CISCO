print("Hisssssss...")


#-----------------------
'''
led = [['###','# #','# #','# #','###'],
       ['  #','  #','  #','  #','  #'],
       ['###','  #','###','#  ','###'],
       ['###','  #','###','  #','###'],
       ['# #','# #','###','  #','  #'],
       ['###','#  ','###','  #','###'],
       ['#  ','#  ','###','# #','###'],
       ['###','  #','  #','  #','  #'],
       ['###','# #','###','# #','###'],
       ['###','# #','###','  #','  #']]
def printled(inp):
    for j in range(5):
        for elem in inp:
            print(led[int(elem)][j], end=" ")
        print()

def readint(prompt):
    while True:
        try:
            inpstr = input(prompt)
            inp = int(inpstr)
            return list(inpstr)
        except ValueError:
            print("You must enter a numeric code.")

inplst = readint("Sample input: ")
printled(inplst)
'''
#-----------------------
'''
# Caesar cipher
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
#-----------------------

# Caesar cipher - decrypting a message
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

#-----------------------
# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
print(strings)
total = 0
try:
    for substr in strings:
        total += float(substr)
    if len(strings) > 0:
        print("The total is:", total)
    else:
        print("The total is:", None)
except:
    print(substr, "is not a number.")
'''
#-----------------------
'''
# IBAN Validator

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
'''
#-----------------------
# Caesar cipher LAB - TIP from course
# input text to encrypt
text = input("Enter message: ")

# enter valid shift value (repeat until it succeeds)
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter cipher's shift (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Bad shift value!")

cipher = ''

for char in text:
    # is it a letter?
    if char.isalpha():
        # shift its code
        code = ord(char) + shift
        # find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # make correction
        code -= first
        code %= 26
        # append encoded character to message
        cipher += chr(first + code)
    else:
        # append original character to message
        cipher += char

print(cipher)

#-----------------------
# Caesar cipher LAB

def shifting(char, shift, begLetter, endLetter):
    code = ''
    realshift = ord(char) + shift - ord(endLetter) 
    if realshift > 0: # case the shift goes after 'z' or 'Z'
        code = ord(begLetter) - 1 + realshift # applies 'a' or 'A' plus remaining of shift after 'z' or 'Z'
    else: # case the shift goes before the 'z' or 'Z'
        code = ord(char) + shift
    return code

def CaesarCipher(text, shift):
    cipher = ''
    for char in text:
        if not char.isalpha(): # changes nothing if char is not a letter
            cipher += char
            continue
        upper = False
        if ord(char) <= ord('Z'): # if char is in upper case
            upper = True
        if upper:
            code = shifting(char, shift, 'A', 'Z')
        else:
            code = shifting(char, shift, 'a', 'z')
        cipher += chr(code)
    return cipher

def readint(prompt, min=1, max=25): 
    while True:
        try:
            inp = int(input(prompt)) # accepts only integer
            assert inp >= min and inp <= max # accepts only in the range
            return inp
        except AssertionError:
            print("Error: the value is not within permitted range (1..25)")
        except ValueError:
            print("You must enter an integer value (1..25)")

while True:
    text = input("Enter your message: ")
    shift = readint("Enter the shift amount (1..25): ")
    ciph = CaesarCipher(text, shift)
    print(ciph)


#-----------------------



