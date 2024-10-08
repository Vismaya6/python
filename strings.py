'''
Author:Vismaya Theresa Benny
version=1.0
Program to access a substring from a given string'''
First_name=input("Enter the first name:")
Last_name=input("Enter the second name:")
full_name=First_name+" "+Last_name
print(full_name)
length=len(First_name)
print(length)
extracted_first_name=full_name[:length]
print(extracted_first_name)