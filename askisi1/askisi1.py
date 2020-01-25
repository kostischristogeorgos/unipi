#PUT THE text.txt file in the same folder as askisi1.py
#Python is 3.7
#1st exercise for the first semester class introduction to programming in UniPi
with open('text.txt', 'r') as file:
    L = file.read().split() #puts all the words from the file in the list
L = (sorted(L, key = len, reverse = True)) #sorts the list based on the lenght of the words
print("5 biggest words in the file")
print("\n")
for i in range(5):
    print(L[i])
print("\n")
print("5 biggest words in the file without vowel letters")
print("\n")
#Removes upper and lower vowel letters
for i in range(5):
    L[i] = (L[i].replace('a', ''))
    L[i] = (L[i].replace('e', ''))
    L[i] = (L[i].replace('i', ''))
    L[i] = (L[i].replace('o', ''))
    L[i] = (L[i].replace('u', ''))
    L[i] = (L[i].replace('A', ''))
    L[i] = (L[i].replace('E', ''))
    L[i] = (L[i].replace('I', ''))
    L[i] = (L[i].replace('O', ''))
    L[i] = (L[i].replace('U', '')) 
    print(L[i])
