'''
Author:Vismaya Theresa Benny
date:15/10/2024
Python program to find final amount after discount
'''
purchase_amount=float(input("Enter the purchase amount:"))
if purchase_amount>500:
    discount=purchase_amount*(20/100)
    Final_amount=purchase_amount-discount
    print("Final amount is:",Final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
    discount=purchase_amount*(10/100)
    Final_amount=purchase_amount-discount
    print("Final_amount is:",Final_amount)
else:
    Final_amount=purchase_amount
    print("Final amount is:",Final_amount)