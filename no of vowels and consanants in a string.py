'''
Author:Vismaya Theresa Benny
Date:29/10/2024
program to find no of vowels and consonants in a string
'''
string_input=input("Enter a String:")
vowels="aeiouAEIOU"
vowels_count=0
consonants=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
    else:
     consonants+=1
print(f"No of consonants in the given string {string_input} is ={consonants}")
print(f"No of vowels in the given sting {string_input} is = {vowels_count}")
