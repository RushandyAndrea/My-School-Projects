#!/usr/bin/env python3

# CSC-365 Crop Calculator Assignment
# This is a program to simulate a cover crop calculator
# Rushandy Andrea is the owner/programmer of this code
# Date: 9/6/2021

print("Cover Crop Calculator")
print()
print("Welcome to the program for Crop Calculator.\n"
      "Easy to use, just type in, and click 'Enter'.")
print()
"""
Here is where I gave the users a friendly display welcome message to the program.
I made it user friendly for every age.
I also made the messages a bit of breathing by giving each pair of sentence a new line, much easier to read.
"""

estimate_length = float(input("Enter the Estimate Length (ft.) of the coverage area here:\t"))
estimate_width = float(input("Enter the Estimate width (ft.) of the coverage area here:\t"))
Seeding_Rate = float(input("Enter the Seeding Rate (lbs) here:\t"))
"""
Here is where I get the input from the users.
I made it as user friendly as i could.
This get input section of the code will also store and use the stored input to calculate.
"""

Acreage = (estimate_length * estimate_width) / 43560
Cover_Crop_Needed = round(Acreage * Seeding_Rate, 2)
"""
Here is where I made the calculation code.
This calculation code will take information from the input of the users to calculate.
"""

print()
print(f"Cover Crop Needed:{Cover_Crop_Needed}")

print()
print("You are now done, bye!")
"""
Here is where I gave it a space first and displayed the calculated Cover Crop that is needed.
By coding to pull the Cover_Crop_Needed in display, it will show the users the exact answer.
And for the last, a message that you are now done.
"""