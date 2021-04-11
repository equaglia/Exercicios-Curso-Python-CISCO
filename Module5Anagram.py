print("Hisssssss...")
'''
def tryAnagram(p1, p2):
    if len(p1) != len(p2):
        print("Not anagrams")
    else:    
        for ele1 in p1:
            print("ele1 =",ele1)
            for i in range(len(p2)):
                print("input2["+str(i)+"] = ",p2[i])
                if ele1.upper() == p2[i].upper():
                    del p2[i]
                    print("input2 = ",p2)
                    break
        if p2 == []:
            print("Anagrams")
        else:
            print("Not anagrams")

def readInput(prompt):
    inpt = ''
    while True:
        try:
            inpt = input(prompt)
            # remove all spaces...
            inpt = inpt.replace(' ','')
            assert inpt != ''
            return inpt
        except AssertionError:
            print("Empty values are not allowed!")
    
while True:
    input1 = list(readInput("Enter first word: "))
    input2 = list(readInput("Enter second word: "))
    print(input1)
    print(input2)
    tryAnagram(input1, input2)
'''
#-----------------------------------
while True:
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # this is what we're going to do with both strings:
    # - remove spaces
    # - change all letters to upper case
    # - convert into list
    # - sort the list
    # - join list's elements into string
    # and finally, compare both strings
    # Let's do it!

    str1 = str1.replace(' ','')
    str2 = str2.replace(' ','')
    str1 = str1.upper()
    str2 = str2.upper()
    str1lst = list(str1)
    str2lst = list(str2)
    str1lst.sort()
    str2lst.sort()
    str1 = ''.join(str1lst)
    str2 = ''.join(str2lst)
    if str1 == str2:
        print("Anagrams")
    else:
        print("Not anagrams")
