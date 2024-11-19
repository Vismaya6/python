'''
Author:Vismaya Theresa Benny
Date:19/10/2024
'''
my_list=[12,13,14,10,10]
unique=[]
for num in my_list:
    if num not in unique:
        unique.append(num)
print("The original list is:",my_list)
print(unique)

