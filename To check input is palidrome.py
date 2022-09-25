for T in range (0,int(input("Please enter no. of test cases you want to perform:-"))):
    a=input("Please enter any no. or word :- ")
    e=0
    l=len(a)
    for i in range (round(l/2)):
        if a[i]==a[-(i+1)]:
            e=e+1
    if e==(round(l/2)):
        print ("YASsss above input is palindrome")
    else:
        print("Na na na me palindrome nhi h...")
print("Pleasure is all mine..")