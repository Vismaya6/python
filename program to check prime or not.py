'''
Author:Vismaya Theresa Benny
Date:29/10/2024
Python program to check prime no or not
'''
number=int(input("Enter a number:"))
isprime=True
for i in range(2,number//2+1):
    if number % i==0:
        isprime=False
        break
if isprime:
    print(f"The given number {number} is prime")
else:
    print(f"The given number {number} is not prime")