#!/usr/bin/env python3

# CSC-365 Crop Calculator Assignment
# This is a program to simulate a cover crop calculator
# Rushandy Andrea is the owner/programmer of this code
# Date: 9/6/2021

"""
Programmer: Rushandy Andrea
Date: 9/6/2021
Description: This is a program to simulate a cover crop calculator
"""

# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = 'September 6, 2021'
__status__ = 'Development'

import validation as val


def crop_calculator():
    """
    This function calculates,  displays welcome message, and take users input to calculate.
    :return: exits a function and instructs Python to continue executing the main program.
    """

    # Here is where I gave the users a friendly display welcome message to the program.
    # I made it user friendly for every age.
    # I also made the messages a bit of breathing by giving each pair of sentence a new line, much easier to read.
    print("Cover Crop Calculator")
    print()
    print("Welcome to the program for Crop Calculator.\n"
          "Easy to use, just type in, and click 'Enter'.")
    print()

    # Here is where I get the input from the users.
    # I made it as user friendly as i could.
    # This get input section of the code will also store and use the stored input to calculate.
    estimate_length = val.get_positive_num(prompt='Enter the Estimate Length (ft.)'
                                                  ' of the coverage area here: ', data_type='float')
    estimate_width = val.get_positive_num(prompt='Enter the Estimate width (ft.)'
                                                 ' of the coverage area here: ', data_type='float')
    seeding_rate = val.get_positive_num(prompt='Enter the Seeding Rate (lbs) here: ', data_type='float')

    # Here is where I made the calculation code.
    # This calculation code will take information from the input of the users to calculate.
    acreage = (estimate_length * estimate_width) / 43560
    cover_crop_needed = round(acreage * seeding_rate, 2)

    # Here is where I gave it a space first and displayed the calculated Cover Crop that is needed.
    # By coding to pull the Cover_Crop_Needed in display, it will show the users the exact answer.
    # And for the last, a message that you are now done.
    print()
    print(f"Cover Crop Needed:{cover_crop_needed}")

    print()
    print("You are now done, bye!")


#  it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
if __name__ == "__crop_calculator__":
    crop_calculator()
