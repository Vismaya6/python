'''
Author:Vismaya Theresa Benny
Date:3/12/2024
pyhton program to define a module to find fibonnacci series
'''
def fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for _ in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence




