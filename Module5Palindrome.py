# Palindrome
while True:
    pali = input("Enter your palindrome: ")
    listpali = list(pali)
    list2 = []
    list1 = []
    listInvert = []
    for elem in listpali: # removing the blank spaces
        if elem != ' ':
            list2.append(elem)
    list1 = list2.copy()
    list1str = ''.join(list1)
    print("string: ",list1str)
    list2.reverse()
    list2str = ''.join(list2)
    print("reverse: ",list2str)
    if list2str.upper() == list1str.upper() and len(list2str) > 1:
        print("palindrome")
    else:
        print("not pali")
    print()

#-----------------------------------
# Palindrome - TIP course
text = input("Enter text: ")

# remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("It's a palindrome")
else:
	print("It's not a palindrome")
