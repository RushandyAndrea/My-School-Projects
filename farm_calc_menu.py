#!/usr/bin/env python3

"""
Programmer: Rushandy Andrea & Caleb Fowler
Date: 6 October, 2021
Description: In farm Calculator Menu, it will put all the other calculators that we have made in class in just one
             program. Users are now able to select the calculator that they need using the Farm Calculator Menu.
             This program will allow the users to navigate through this Calculator to another calculator and back to
             this calculator menu.
"""


# Here is where the author's authorship including the date, version and status of the programmer.
# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = 'October 6, 2021'
__status__ = 'Development'


# Here  is where I put all the imports to be loaded in this Farm Calculator program.
import break_even_calc as bec
import crop_calculator as cc
import farm_calc_help as fch
import stocking_rate_calc as src
import water_allocations_calc as wac

LINE_LENGTH = 112


def welcome():
    """
    This function displays a welcome message to user.
    :return: exits a function and instructs Python to continue executing the main program.
    """
    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('                        *the Farmers calculators*')
    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('To make use of this calculator, you will need to type in the following data below.')
    print('Please insert a number value that is given by the program, otherwise it will show you error.')
    print(f'_' * LINE_LENGTH)


def display_menu():
    """
    This function displays the options that the user can choose from.
    Here is where I define and call the display_menu, and main which users can read and decide what to do.
    In main the command is taking the input from the users, and if user type in any number asked by the program,
    the program will execute the right program that the user inserted/typed.
    :return: exits a function and instructs Python to continue executing the main program.
    """
    print(f'_' * LINE_LENGTH)
    print('The Farmers Calculators')
    print(f'=' * LINE_LENGTH)
    print('Command Menu')
    print('1 - Break Even Calculator')
    print('2 - Crop Calculator')
    print('3 - Stocking Rate Calculator')
    print('4 - Water Allocations Calculator')
    print('5 - Help')
    print('6 - Help (user-friendly)')
    print('7 - Quit Program')
    print()


def main():
    """
    This function take and execute the options from the user.
    :return:  exits a function and instructs Python to continue executing the main program.
    """
    while True:
        display_menu()
        command = int(input("Command: "))
        if command == 1:
            bec.break_even_calc()
        elif command == 2:
            cc.crop_calculator()
        elif command == 3:
            src.stocking_rate_calc()
        elif command == 4:
            wac.water_allocations_calc()
        elif command == 5:
            help('farm_calc_menu')
        elif command == 6:
            fch.main()
        elif command == 7:
            break
        else:
            print('Error, please type a number for one of the 6 commands.')

        print()
        print(f'=' * LINE_LENGTH)
        input('Press any key to continue...')

    print('Bye!')


# it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
if __name__ == "__main__":
    main()
