# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

import math

def CalculateDistance():
    
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
   
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    

    print(f"The distance between the two  points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")

CalculateDistance()





# Question 1(ii)
# Write a Python program to find maximum between three numbers.

num1 = float(input('Please enter the firt number: '))
num2 = float(input('Please enter the second number: '))
num3= float(input('Please enter the third number: '))

if num1 > num2:
    print('Number 1 is the greatest')
elif num2 > num3:
    print('Num 2 is greatest')
else:
    print('Num 3 is greatest')



