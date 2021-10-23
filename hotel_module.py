#!/usr/bin/env python3

import random

import validation as val
from main import main

LINE_LENGTH = 112


def welcome_message():
    """
    Here is where I introduce the user to the program, and give the option to choose from.
    :return: none
    """
    print()
    print(f'*' * LINE_LENGTH)
    print()
    print('                        *Python Programmer’s Paradise - Motel Booking System!*')
    print()
    print(f'*' * LINE_LENGTH)

    print(f'_' * LINE_LENGTH)
    print('Which day of the week will you be checking in?')
    print()
    print('Sunday, Monday, Tuesday = Command 1')
    print('Wednesday and Thursday  = Command 2')
    print('Friday and Saturday     = Command 3')
    print()
    print(f'=' * LINE_LENGTH)


# not sure of this, just freestyling until it works ('o__0)
def get_dow():
    """
    prompt the user for what dow they want to check in & validate (1-7)
    :return: dow
    """
    dow = val.get_range(prompt='type in the days category number you would like to book:  ', low=0, high=3)
    while True:
        if dow == 1:
            print('You have chosen category 1 which is Sunday, Monday, and Tuesday.')
            return dow
        elif dow == 2:
            print('You have chosen category 2 which is Wednesday and Thursday.')
            return dow
        elif dow == 3:
            print('You have chosen category 3 which is Friday and Saturday.')
            return dow
        else:
            print('Error, please type a number from 1 to 3 only.')
            exit()


print()
print(f'-' * LINE_LENGTH)
print()


def get_dow_rate(dow):
    """
    calculate the dow_rate based on dow end the program if an invalid dow is received
    :return: base rate
    """
    base_rate = 80
    cat1 = base_rate + 16
    cat2 = base_rate + 8
    cat3 = base_rate
    dow = input(' \n'
                'To check the rates of your desired day of booking, '
                'please type in: \n'
                '"cat1" for Sunday, Monday, and Tuesday \n'
                '"cat2" for Wednesday and Thursday \n'
                '"cat3" for Friday and Saturday \n'
                'Please type your category here: ').lower()
    while True:
        if dow == 'cat1':
            print(f'The total amount for your booking is: ${cat1}')
            return base_rate * 1.2
        elif dow == 'cat2':
            print(f'The total amount for your booking is: ${cat2}')
            return base_rate * 1.1
        elif dow == 'cat3':
            print(f'The total amount for your booking is: ${cat3}')
            return base_rate
        else:
            print('Error, please type in cat1 or cat2 or cat3 only!')
            exit()


def get_avail_rooms():
    """

    :return:
    """
    num_single = random.randint(0, 8)
    num_double = random.randint(0, 10)
    num_king = random.randint(0, 2)

    return num_single, num_double, num_king


def get_room_rates(dow_rate):
    """
    This function calculate rate of single, double, and king rate variables.
    :param dow_rate: This function takes the parameter dow_rate to use it for the calculation
    :return: single_rate, double_rate, king_rate
    """

    single_rate = dow_rate
    double_rate = dow_rate * 1.5
    king_rate = dow_rate * 1.25

    return int(single_rate), int(double_rate), int(king_rate)


def get_room_type_rate(dow, dow_rate):
    """
    calculate rates based on type
    :param dow:
    :param dow_rate:
    :return: single_rate, double_rate, king_rate
    """
    num_single, num_double, num_king = get_avail_rooms()
    single_rate, double_rate, king_rate = get_room_rates(dow_rate)
    print()
    print(f'There are {dow} available Rooms')
    print(f'-' * LINE_LENGTH)
    print(f'There are {num_single} single rooms (2 guest max) available at ${single_rate} only!')
    print(f'There are {num_double} double rooms (4 guest max) available at ${double_rate} only!')
    print(f'There are {num_king} king rooms (2 guest max) available at ${king_rate} only!')
    print()
    print('Choose your desire available room: ')

    room_type = val.get_range(prompt='1 = Single, 2 = Double, 3 = King: ', low=0, high=3)
    while True:
        if room_type == 1:
            return room_type, single_rate
        elif room_type == 2:
            return room_type, double_rate
        elif room_type == 3:
            return room_type, king_rate
        else:
            print('Error, please type in a number between 1 - 3 only.')
            break


def get_num_guests(room_type):
    """

    :param room_type:
    :return: num_guest
    """
    if room_type == 1:
        print()
        num_guests = val.get_range(prompt=f'How many guests will be staying in the type {room_type} room: ', low=1,
                                   high=2)
        return num_guests
    elif room_type == 2:
        print()
        num_guests = val.get_range(prompt=f'How many guests will be staying in the type {room_type} room: ', low=1,
                                   high=4)
        return num_guests
    else:
        print('There has been an error.')
        exit()


def get_surcharge(num_guests):
    """
    calculate the surcharge
    :return: one_person, two_person, three_person, four_person
    """
    num_people = int(input(f'The amount of guest in room are: {num_guests} (4 max)'))
    one_person = 0
    two_person = 10
    three_person = 18
    four_person = 32

    if num_people == 1:
        print(f'${one_person} surcharge')
        return one_person
    elif num_people == 2:
        print(f'${two_person} surcharge')
        return two_person
    elif num_people == 3:
        print(f'${three_person} surcharge')
        return three_person
    elif num_people == 4:
        print(f'${four_person} surcharge')
        return four_person
    else:
        print("Error, please type in a number between 1 and 4!")
        exit()


def get_number_of_nights(room_type, num_guests, total_room_rate):
    """

    :param room_type:
    :param num_guests:
    :param total_room_rate:
    :return: num_nights
    """
    num_nights = val.get_positive_num(
        prompt=f'How many nights will you want to book a type {room_type} room, \n'
               f'with {num_guests} guests '
               f'at the rate of ${room_type}: ', data_type='int')
    print(f'Total room rate = ${total_room_rate}')

    return num_nights


def confirm_booking(num_nights, total_charge):
    """

    :param num_nights:
    :param total_charge:
    :return:
    """
    while True:
        print(f'Number of nights = {num_nights}')
        print(f'Total charge = ${total_charge}')

        end_user_y_n = input('Booking confirmation. Do you confirm your booking? y = yes, n = no: ').lower()

        if end_user_y_n == 'y':
            print('Thank you for booking to our hotel. Bye!')
            exit()
        elif end_user_y_n == 'n':
            print(main())
            break

        else:
            print('Error, please insert a y or n only!'
                  'Program shutting down.')
            exit()


def display_booking(dow, dow_rate, room_type, room_type_rate, num_guests, surcharge):
    """

    :param dow:
    :param dow_rate:
    :param room_type:
    :param room_type_rate:
    :param num_guests:
    :param surcharge:
    :return:
    """
    print(f'Your dow = {dow}')
    print(f'Your dow rate = {dow_rate}')
    print(f'Your room type = {room_type}')
    print(f'Your room type rate = {room_type_rate}')
    print(f'Your number of guests = {num_guests}')
    print(f'Your surcharge = {surcharge}')


def get_do_you_want_to_continue():
    """
    prompt the user if they want to book another room (lower case input and validate: y, n, yes, no)
    :return: true or false
    """
    user_input = input('Do you want to continue? y=Yes  n=No: ').lower()
    while True:
        if user_input == 'y':
            import main
            print(main)
            return get_do_you_want_to_continue()

        elif user_input == 'n':
            print('Thank you for using our Help program!')
            import main
            print(main)
            return get_do_you_want_to_continue()

        else:
            print('Error, please insert a y or n only!'
                  'Program needs to be restarted.')
            break
