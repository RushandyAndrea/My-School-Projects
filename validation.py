#!/usr/bin/env python3

# I am not done with hotel_module
def get_range(prompt, low, high, data_type='int'):
    """
    This function checks if the user inserted a number that is in the range of
    the lowest(1) asked and in the highest(7) asked. By using a while loop to get the user to insert a
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

        if low <= number <= high:
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

def confirm_booking(num_nights, total_charge):
    """

    :param num_nights:
    :param total_charge:
    :return:
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


def get_yes_no():
    """
       Here is where the function ask for user input.
       :return: exits a function and instructs Python to continue executing the main program.
       """
    choice = 'y'
    while choice.lower() == 'y':
        # see if the user wants to continue
        choice = input('Do you want to continue? (y/n: ')
        print()

    print('Bye!')
