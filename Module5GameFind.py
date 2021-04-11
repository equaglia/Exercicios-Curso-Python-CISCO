while True:
    short = input("Enter first string: ")
    #long = input("Enter second string: ")
#    long = "vcxzxduybfdsobywuefgas"
    long = "Nabucodonosor"
    print(long)
    init = 0
    end = 0
    aux = 0
    for letter in short:
        while init <= end and init != -1:
#            print(letter, end=' ')
#            print("init = ",init, end = ' ')
#            print("aux = ",aux)
            aux = long.find(letter, init)
            print(aux)
            if aux > init or aux == -1:
                init = aux
        end = init
    if init == -1:
        print("No")
    else:
        print("Yes")
    print()

#-----------------------------------
# Hint solution LAB
word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")
