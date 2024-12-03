'''
Author:Vismaya Theresa Benny
Date:3/12/2024
python program to find factorial using recursion
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
f=factorial(5)
print(f)