#!/usr/bin/env python3

"""
Programmer: Rushandy Andrea & Caleb Fowler
Date: 15 October, 2021
Description: .
"""

# Here is where the author's authorship including the date, version and status of the programmer.
# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = '15 October, 2021'
__status__ = 'Development'

import hotel_module

LINE_LENGTH = 112


def main():
    """
    This function take and execute the options from the user.
    :return:  exits a function and instructs Python to continue executing the main program.
    """
    hotel_module.welcome_message()
    loop = True
    grand_total_charge = 0
    while loop:
        dow = hotel_module.get_dow()
        dow_rate = hotel_module.get_dow_rate(dow)

        room_type, room_type_rate = hotel_module.get_room_type_rate(dow, dow_rate)
        num_guests = hotel_module.get_num_guests(room_type)

        surcharge = hotel_module.get_surcharge(num_guests)
        total_room_rate = room_type_rate + surcharge

        num_nights = hotel_module.get_number_of_nights(room_type, num_guests, total_room_rate)
        total_charge = total_room_rate * num_nights

        book_another = hotel_module.confirm_booking(num_nights, total_charge)
        if book_another in ['yes', 'y']:
            grand_total_charge += total_charge

        loop = hotel_module.get_do_you_want_to_continue()


if __name__ == "__main__":
    main()
