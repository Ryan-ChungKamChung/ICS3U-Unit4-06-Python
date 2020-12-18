#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program displays every possible RGB value


import constants


def main():
    # this function displays every possible RGB value

    loop_counter1 = 0
    loop_counter2 = 0
    loop_counter3 = 0

    # Process and Output
    for loop_counter1 in range(constants.MAX_VALUE + 1):
        for loop_counter2 in range(constants.MAX_VALUE + 1):
            for loop_counter3 in range(constants.MAX_VALUE + 1):
                print("RGB({0},{1},{2})".format(loop_counter1, loop_counter2,
                                                loop_counter3))


if __name__ == "__main__":
    main()
