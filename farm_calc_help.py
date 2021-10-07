#!/usr/bin/env python3

# This is the Farm Calculator Help header. Displaying a sort of encouraging message to the user.

"""
programmer
date
description:

"""


LINE_LENGTH = 112


def welcome():

    print(f'-' * LINE_LENGTH)
    print()
    print('Welcome to Help section!')
    print()
    print('Do not feel helpless, we can help you with anything related to this program.')
    print()
    print(f'-' * LINE_LENGTH)
    print()


# Here is where I will ask the user some of the possible things that someone might need help with.
# I will put more than 3 option for the user to choose from.


def main():
    print('Here are few common questions option to choose from.')
    print()
    print('Command Menu')
    print('1 - How do you restart this program?')
    print('2 - My Calculators are not displaying.')
    print('3 - How to undo?')
    print('4 - My cat pressed few buttons, and now it is showing me error.')
    print('5 - How do I contact for other type of question?')
    print('6 - Quit Help')
    print()

    while True:
        user_input = int(input('Here you can type in the option number you want here: \t'))

        if user_input == 1:
            print('You can simply type in #6 to quit Help and restart the program')

        elif user_input == 2:
            print('Make sure you selected one of the calculators that we offered you, we can not show you every')
            print('calculator at once.')

        elif user_input == 3:
            print('You can not undo directly, but you can simply choose a number again.')

        elif user_input == 4:
            print('You can retype the option number you want to. If that does not work, ')
            print('close the program and open it again')

        elif user_input == 5:
            print('You can visit our online website: www.FarmCalculator.com/help')

        elif user_input == 6:
            print('Bye!')
            break

        else:
            print('Error, make sure you type in a number and between 1 and 6.')

        while True:
            end_user_y_n = input('Do you want to run continue using Help? y = yes, n = no: ').lower()

            if end_user_y_n == 'y':
                print(main())
                break

            elif end_user_y_n == 'n':
                print('Thank you for using our Help program!')
                import farm_calc_menu
                print(farm_calc_menu)
                break

            else:
                print('Error, please insert a y or n only!'
                      'Program needs to be restarted.')
                break


#  it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
if __name__ == "__main__":
    main()
