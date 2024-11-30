'''
Author:Vismaya Theresa Benny
Date:30/11/2024
pyhton program to check the given sides are the part of the right angle triangle or not
'''
def is_right_angle_triangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        return True
    return False
side1=int(input("Enter the side1:"))
side2=int(input("Enter the side2:"))
side3=int(input("Enter the side3:"))
if is_right_angle_triangle(side1,side2,side3):
    print(f"The given sides are part of the right angle triangle")
else:
    print(f"The given sides are not part of the right angle triangle:")





