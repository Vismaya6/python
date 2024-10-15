'''
Author:Vismaya Theresa Benny
date:15/10/2024
Python program to determine the entry ticket fare
'''
age=int(input("Enter the age:"))
if age<10:
    print("fare=7")
elif age>=10 and age<60:
    print("fare=10")
else:
    print("fare=5")