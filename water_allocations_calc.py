#!/usr/bin/env python3

"""
# Programmer: Rushandy Andrea & Caleb Fowler
# Date: September 26, 2021
# Description: In this assignment we had to work in group of 2. We had to write a code that will be calculating
#              the water allocation for the user. Keeping in mind that we need to make this program
#              most user friendly as possible. Using while loop in a while loop and validate each variable.
"""

# Authorship
__author__ = 'Rushandy Andrea, Caleb Fowler'
__version__ = '1.0'
__date__ = 'Sept 26, 2021'
__status__ = 'Development'

import validation

LINE_LENGTH = 112


def water_allocations_calc():
    # Display a welcome message to user and define LINE_LENGTH at the top.
    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('                        *Welcome to Water Allocations Calculator*')
    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('To make use of this calculator, you will need to type in the following data below.')
    print('Please insert a number value that is more than 0 only, otherwise it will show you error.')
    print(f'_' * LINE_LENGTH)

    # Input from the user, calls the if else statement input of the user and validates each and every single variable
    # with a number above 0, else, throw an error.
    while True:

        while True:
            ration_alloc_depth = validation.get_range(prompt='Enter the rationed allocation '
                                                             'depth in inches: ', low=0, high=99999999)

            if ration_alloc_depth > 0:
                break
            else:
                print('Error, please insert a number value more than 0')

        while True:
            area_irrigated_acres = validation.get_range(prompt='Enter the area being '
                                                               'irrigated in acres: ', low=0, high=99999999)

            if area_irrigated_acres > 0:
                break
            else:
                print('Error, please insert a number value more than 0')

        while True:
            aver_rate_flow = validation.get_range(prompt='Enter the average '
                                                         'rate of flow in U.S. gpm: ', low=0, high=99999999)

            if aver_rate_flow > 0:
                break
            else:
                print('Error, please insert a number value more than 0')

        print()
        print(f'=' * LINE_LENGTH)

        # Calculation of the program will be coded in this section
        alloc_time_delivery = round((18.857 * ration_alloc_depth * area_irrigated_acres) / aver_rate_flow, 1)
        print(f'The allocation of water will be used up in *{alloc_time_delivery}* days when ')
        print(f'*{area_irrigated_acres}* acres is irrigated with an irrigation system that ')
        print(f'has a U.S. gallon per minute of *{aver_rate_flow}* system capacity ')
        print(f'and the rationed allocation depth is *{ration_alloc_depth}* inches.')
        print(f'')

        end_user_input = input('Do you want to run a new calculation? y = yes, n = no: ').lower()

        # if and elseif for continuing or breaking out of the calculator
        if end_user_input == 'y':
            print()
            continue
        elif end_user_input == 'n':
            print('Thank you for using our Calculator program!')
            break
        else:
            print('Error, please insert a y or n only!\n '
                  'Program needs to be restarted.')


if __name__ == "__water_allocations_calc__":
    water_allocations_calc()
