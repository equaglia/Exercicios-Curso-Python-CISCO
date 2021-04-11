print("Hisssssss...")

# The Digit of Life LAB

def readint(prompt, digits=8): 
    while True:
        try:
            inp = int(input(prompt)) # accepts only integer 8 digits
            assert len(list(str(inp))) == 8
            return inp
        except AssertionError:
            print("You must enter an integer value (format YYYYMMDD)")
        except ValueError:
            print("You must enter an integer value (format YYYYMMDD)")

while True:
    bdate = readint("Enter your birthdate (format YYYYMMDD): ")
    bdatelst = list(str(bdate))
    oneDigit = False
    while not oneDigit:
        sumdate = 0
        for elem in bdatelst:
            sumdate += int(elem)
        bdatelst = list(str(sumdate))
        if len(bdatelst) == 1:
            print("The Digit of Life is ", int(bdatelst[0]))
            oneDigit = True
    
#-----------------------
