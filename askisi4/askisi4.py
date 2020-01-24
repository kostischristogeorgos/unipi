#4th exercise for the first semester class introduction to programming in UniPi
#Python is 3.7

def calculation(x):
    L=[]
    number = ''
    # puts every character's ascii hex in a list
    for i in x:
        L.append(ord(i))
    print(L)

    # creates the number by putting all the numbers from the list in line
    for i in range(len(L)):
        number = str(number) + str(L[i])

    #makes the number int again
    number = int(number)

    # only numbers larger than 1 are prime numbers
    if number > 1:
        #checks every number to see if it it's mod is equal to 0, if true, it breaks
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number because", number, "/", i, "=", number // i, "which is an int")
                break
        # if code doesn't break, number is a prime number
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

#Calls the function
x = input("Give a string")
calculation(x)
