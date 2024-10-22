'''
Author:Vismaya Theresa Benny
Date:22/10/2024
python program to find largest of three number's
'''
No1=int(input("Enter the first no:"))
No2=int(input("Enter the second no:"))
No3=int(input("Enter the third no:"))
if (No1>No2 and No1>No3):
    print("The largest number is:",No1)
elif(No2>No3):
    print("The largest number is",No2)
else:
    print("Largest number is:",No3)
