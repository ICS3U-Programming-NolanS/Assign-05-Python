#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Dec 11th 2022
# This program calculates the volume
# of the user's cone through the user's given radius and height.


import math

def calc_cone():

    try:
        # converts user's radius and height to float
        user_radius_float = float(
            input("Please enter your chosen radius of your cone: ")
        )
        user_height_float = float(
            input(
                "Please enter your chosen height of your cone: "
            )
        )
        print("")
        # calculates the volume through using user's given radius and height
        user_volume = math.pi * (user_radius_float * user_radius_float) * (user_height_float / 3)
        # displays answer
        print(
            "With {:,.2f} being the radius and {:,.2f} being the height, the volume of your cone is: {:,.2f} cubed !".format(
                user_radius_float, user_height_float, user_volume
            )
        )
    # exception in order to catch any erroneous/invalid input
    except Exception:
        print("I feel like you didn't enter a number...YOU MUST ENTER A NUMBER!!!")


# displays main which calls a function
def main():
    calc_cone()


if __name__ == "__main__":
    main()