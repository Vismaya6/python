'''
Author:Vismaya Theresa Benny
date:15/10/2024
Python program to print n odd numbers
'''
limit=int(input("Enter the limit:"))
count=0
odd_number=1
while count<limit:
    print(odd_number,"\t",end=" ")
    count+=1
    odd_number+=2