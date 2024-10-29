'''
Author:Vismaya Theresa Benny
Date:29/10/2024
Program to print prime no's upto alimit
'''
limit=int(input("Enter a limit:"))
for number in range (2,limit+1):
    isprime=True
    for i in range (2,number//2+1):
        if number%i==0:
            isprime = False
    if isprime:
     print(number)