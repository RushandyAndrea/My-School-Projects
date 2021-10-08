#!/usr/bin/env python3

"""
Description: This is the validation program. It is used to check if the input data type is correct or not.
             It can be used to check if there are no invalid values in the given input.
             Validation in python can be used to check if the given input is valid.
"""

# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = 'October 6, 2021'
__status__ = 'Development'


def get_range(prompt, low, high, data_type='int'):
    """
    This function checks if the user inserted a number that is in the range of
    the lowest asked and in the highest asked. By using a while loop to get the user to insert a
    data or to close the program.
    :param prompt: a string that will be printed on the screen whenever the function is called.
    :param low: two variables; low and high. These variables are defined by their position.
    :param high: two variables; low and high. These variables are defined by their position.
    :param data_type: data types are the classification or categorization of data items. It represents
                      the kind of value that tells what operations can be performed on a particular data.
    :return: exits a function and instructs Python to continue executing the main program.
    """

    while True:
        user_input = input(f'{prompt} (Range = {low}-{high}): ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if low < number <= high:
            return number
        else:
            print('Entry must be greater than', low,
                  'and less than or equal to', high)


def get_positive_num(prompt, data_type='int'):
    """
    This function checks if the user inserted a number greater than 0. By using a while loop to get the user to insert a
    data or to close the program.
    :param prompt: a string that will be printed on the screen whenever the function is called.
    :param data_type: data types are the classification or categorization of data items. It represents
                      the kind of value that tells what operations can be performed on a particular data.
    :return: exits a function and instructs Python to continue executing the main program.
    """

    while True:
        user_input_positive = input(f'{prompt} Insert a number greater than 0: ')

        if data_type == 'int':
            number_positive = int(user_input_positive)
        else:
            number_positive = float(user_input_positive)

        if number_positive > 0:
            return number_positive
        else:
            print('Please enter a number that is greater than zero!')
            continue


def get_num():
    """
    This function checks if the user has typed in a number and not anything else.
    :return: exits a function and instructs Python to continue executing the main program.
    """

    while True:

        value = input('Write a number: ')
        if value == int(value):
            break
        else:
            print('That is not a number,enter a number, please')
            continue


def main():
    """
    Here is where the function ask for user input.
    :return: exits a function and instructs Python to continue executing the main program.
    """
    choice = 'y'
    while choice.lower() == 'y':
        # get input
        valid_numb = get_range(prompt='Enter float', low=0, high=1000, data_type='float')
        print('Valid number = ', valid_numb)
        print()
        valid_numb = get_range(prompt='Enter int', low=0, high=1000, data_type='int')
        print('Valid integer = ', valid_numb)
        print()
        valid_numb = get_positive_num(prompt='Enter a positive number only', data_type='int')
        print('Valid number = ', valid_numb)
        # see if the user wants to continue
        choice = input('Do you want to continue? (y/n: ')
        print()

    print('Bye!')


#  it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
if __name__ == '__main__':
    main()
