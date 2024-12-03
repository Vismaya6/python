'''
Author:Vismaya Theresa Benny
Date:3/12/2024
python program to find product using recursion
'''

def mul_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mul_numbers(n1,n2-1)
mul=mul_numbers(5,4)
print(mul)