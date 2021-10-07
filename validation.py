#!/usr/bin/env python3

"""

"""


# description needed here
def get_range(prompt, low, high, data_type='int'):
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


# docstrings needed
def get_positive_num(prompt, data_type='int'):
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


def get_num(prompt, data_type='int'):
    """

    :param prompt:
    :param data_type:
    :return:
    """
    while True:
        user_input_num = input(f'{prompt} Insert a number: ')

        if data_type == 'int':
            num = int(user_input_num)
        else:
            user_input_num = float(user_input_num)


def main():
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
