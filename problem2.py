"""
-------------------------------------------------------------------------------
Name: problem2.py
Purpose: 
Author: Schwarenberg.M
Created: 23/02/2021
------------------------------------------------------------------------------
"""

 # Welcome message
print("Welcome to the Triangle Checker")
print("---")

 # Input triangle sides
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))
print("---")

 # processing and output of data
if side1 + side2 >= side3:
  print("The figure is a triangle.")
elif side1 + side3 >= side2:
  print("The figure is a triangle.")
elif side3 + side2 >= side1:
  print("The figure is a triangle.")
else:
  print("The figure is NOT a triangle.")