"""
-------------------------------------------------------------------------------
Name: problem1.py
Purpose: To help NASA's Perseverance Rover identify martian class based off of physical appearance. 
Author: Schwarenberg.M
Created: 23/02/2021
------------------------------------------------------------------------------
"""

 # Input the data
antenna = int(input("How many antennas?: "))
eyes = int(input("How many eyes?: "))

 # Processing of data and display
if antenna == 0 and eyes == 2:
  print("Life form detected: MattDamonMartian")

elif antenna <= 2 and eyes <= 3:
  print("Life form detected: BrooklynMartian")

elif antenna >= 3 and eyes <= 4:
  print("Life form detected: AudreyMartian")

elif antenna <= 6 and eyes >= 2:
  print("Life form detected: MaxMartian")

else:
  print("No life form detected")