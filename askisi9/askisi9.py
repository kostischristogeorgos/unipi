#9th exercise for the first semester class introduction to programming in UniPi
x = int(input("Give me a number"))
number = 3*x + 1
numlist = [int(x) for x in str(number)] #Puts every digit of the number in the list
s = 0
for i in range(0, len(numlist)): #adds up all the digits in the list
    s = s + numlist[i]

print("\n3*", x, "+ 1 =", number,"and the sum of its digits =",s)
print(s, "isn't a single-digit")

while(s >=10): #while the sum is larger or equal to 10, the loop continues
    print("\n")
    x = int(input("Give a number again"))
    number = 3*x + 1
    numlist = [int(x) for x in str(number)]
    s = 0
    for i in range(0, len(numlist)):
        s = s + numlist[i]
    print("\n3*", x, "+ 1 =", number,"and the sum of its digits =",s)
    if s >= 10:
        print("\n",s, "isn't a single-digit")
print("\nThe program ended because the sum of the digits of",number,"is equal to",s,"which is single-digit")
