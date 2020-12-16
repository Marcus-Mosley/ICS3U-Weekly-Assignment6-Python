#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on December 2020
# This program calculates the surface area and volume of a octagonal prism

import math


def s_area(base_int, height_int):
    # This functions calculates surface_area

    surface_area = (8.0 * base_int * height_int + 4.0
                    * (1 + math.sqrt(2.0)) * base_int**2.0)

    return surface_area


def vol(base_int, height_int):
    # This functions calculates volume

    volume = 2.0 * (1.0 + math.sqrt(2.0)) * height_int * base_int**2.0

    return volume


def main():
    # This function receives input

    # Input
    while True:
        base_str = input("Enter Length of the Base Edge of the Octagonal"
                         " Prism (mm): ")
        try:
            base_int = float(base_str)
        except Exception:
            print("That is not a number, please input a number!")
            print("")
        else:
            if base_int <= 0:
                print("You have not inputted a valid base length, please input"
                      " a positive number!")
                print("")
            else:
                break
    while True:
        height_str = input("Enter Height of the Octagonal Prism (mm): ")

        try:
            height_int = float(height_str)
        except Exception:
            print("That is not a number, please input a number!")
            print("")
        else:
            if height_int <= 0:
                print("You have not inputted a valid base length, please input"
                      " a positive number!")
                print("")
            else:
                break
    print("")

    # Call Functions
    surface_area = s_area(base_int, height_int)
    volume = vol(base_int, height_int)

    # Output
    print("")
    print("Surface Area is {0:.2f}mm^2".format(surface_area))
    print("Volume is {0:.2f}mm^3".format(volume))


if __name__ == "__main__":
    main()
