x=int(input("Please enter any number to check prime no."))
c=0
d=0
for i in range (2,x):
    if (x%i)==0:
        d=1
        print(i)
        break
if d==1:
    print("Given no. is not prime. It is divisible by ",i)
else:
    print("prime")
