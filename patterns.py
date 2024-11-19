number=int(input("Enter a number:"))
for i in range(number):
    for j in range(i):
        print("*",end=" ")
    print()


number=int(input("Enter a number:"))
for i in range(number,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


number = int(input("Enter a number:"))
for i in range(1,number):
    for j in range(number-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

number=int(input("Enter a number:"))
for i in range(number-1,0,-1):
    for j in range(number-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()