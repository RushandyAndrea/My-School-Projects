#!/usr/bin/env python3

"""
# Programmer: Rushandy Andrea
# Date: September 19, 2021
# Description: In this project, I will be coding a calculator that will help determine how many
# cow-calf pairs a pasture can support per acre of forage.
"""

# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = 'Sept 19, 2021'
__status__ = 'Development'

import validation

LINE_LENGTH = 112


def stocking_rate_calc():
    # Display a welcome message to user and define LINE_LENGTH at the top.

    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('                        *Welcome to Cow-Calf Pair Pasture Stock Rate Calculator*')
    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('To make use of this calculator, you will need to type in the following data below.')
    print(f'_' * LINE_LENGTH)

    # Input from the user, calls the if else statement input of the user between 1 and 20.
    while True:
        num_sample_taken = validation.get_range(prompt='Please enter the # of forage samples '
                                                       'taken: ', low=0, high=20)

        if 1 <= num_sample_taken <= 20:
            break
        else:
            print('Invalid value! (Valid value = 1-20)')
    print()
    print(f'=' * LINE_LENGTH)

    # Display dry clipping in grams and make a for statement for the input of the user.
    print()
    print('Please enter dry clipping in grams: ')
    print()

    dried_forage_weight = 0
    for i in range(0, 5):
        dried_forage_weight += int(input(f'Sample #{i + 1}: '))

    # Calculate and display square foot avg lbs by calculating square foot expression to 3 decimals positions.
    print()
    square_foot_avg_lbs = round((dried_forage_weight / num_sample_taken) / 453.592, 3)
    print(f'The average square foot per pound: {square_foot_avg_lbs}')
    forage_per_acre = round(square_foot_avg_lbs * 43560, )
    print(f'The average forage per acre in pound: {forage_per_acre}')
    print()
    print(f'_' * LINE_LENGTH)
    print()

    # Input from the user, calls the if else statement input of the user between 1 and 100.
    while True:
        utilization_rate = validation.get_range(prompt='Please enter the utilization rate:  ', low=0, high=100)

        if 1 <= utilization_rate <= 100:
            break
        else:
            print('Invalid value! (Valid value = 1-100)')
    print()

    # Input from the user, calls the if else statement input of the user between 1 and 2000.
    while True:
        aum = validation.get_range(prompt='Please enter the animal unit:  ', low=0, high=2000)

        if 1 <= aum <= 2000:
            break
        else:
            print('Invalid value! (Valid value = 1-2000)')
    print()
    print(f'*' * LINE_LENGTH)
    print()

    # Calculate and display stocking rate and round to 2 decimal positions, and display
    # the end of the program for the user.
    stocking_rate = round((forage_per_acre * utilization_rate / 100) / aum, 2)
    print(f'Stocking rate (cow-calf per acre): {stocking_rate}')
    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('Thank you for using Cow-Calf Pair Pasture Stock Rate Calculator!')
    print('Bye!')
    print()
    print(f'#' * LINE_LENGTH)


#  it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
if __name__ == "__stocking_rate_calc__":
    stocking_rate_calc()
