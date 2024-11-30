'''
Author:Vismaya Theresa Benny
Date:30/11/2024
pyhton program to check a mobile number is valid or not
'''
def check():
    number=(input("Enter number:"))
    d=len(number)
    if d==10:
        if number[1]=="7" or number[1]=="8" or number[1]=="9":
            print("Valid")
        else:
            print("invalid")
    else:
        print("invalid")
check()


