'''
Author:Vismaya Theresa Benny
Date:3/12/2024
python program to find sum using recursion
'''

def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
sum=add_numbers(5,4)
print(sum)