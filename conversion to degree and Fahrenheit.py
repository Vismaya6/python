'''
Author:Vismaya Theresa Benny
Date:22/10/2024
python program to convert Celsius to Fahrenheit and Fahrenheit to Celsius
'''
temp=float(input("Enter the temperature:"))
unit=input("Is this in (C)elsius or in (F)ahrenheit?")
if (unit=="C"):
    F=((9/5*temp)+32)
    print(temp,"Celsius is",F,"Fahrenheit.")
else:
    C=(5/9*(temp-32))
    print(temp,"Fahrenheit is",C,"Celsius.")
