'''
Author:Vismaya Theresa Benny
date:15/10/2024
Python program to find sum of the digits of a given number
'''
number=int(input("Enter the number:"))
sum=0
while number>0:
    r=number%10
    number=number//10
    sum=sum+r
print("sum of the digits:",sum)