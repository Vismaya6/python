'''
Author:Vismaya Theresa Benny
date:15/10/2024
Python program to find smallest among three
'''
Num1=int(input("Enter first no:"))
Num2=int(input("Enter the sec no:"))
Num3=int(input("Enter the third no:"))
if Num1<Num2 and Num1<Num3:
    print(Num1)
elif Num2<Num3:
    print(Num2)
else:
    print(Num3)

