'''
Author:Vismaya Theresa Benny
Date:30/11/2024
pyhton program to check count
'''
def count_upper_lower_case_characters(input_string):
    upper_count=0
    lower_count=0
    for i in input_string:
        if i .isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    return upper_count,lower_count
input_string=input("Enter a string:")
upper_count,lower_count=count_upper_lower_case_characters(input_string)
print((upper_count))
print(lower_count)






