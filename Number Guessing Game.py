import random as rd
n=rd.randint(0,100)
for i in range (10**2):
    x = int(input("Please guess no. "))
    if n==x:
        print("Congress you win..❤")
        print("Chance taken = ",i+1)
        break
    elif x>n:
        print("Guessed no. is high..\n Please try again.")
    else:
        print("Guessed no. is low..\n Please try again.")