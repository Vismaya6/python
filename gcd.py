'''
Author:Vismaya Theresa Benny
Date:3/12/2024
python program to find gcd using recursion
'''

def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
gcd=gcd(516,188)
print(gcd)
