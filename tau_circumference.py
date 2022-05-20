#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


def main():
    # I calculate circumference

    # input
    str_repeat_number = input("Enter how many times to repeat: ")
    print("")

    # process
    try:
        int_repeat_number = int(str_repeat_number)
        if int_repeat_number < 0:
            raise Exception()
        else:
            for counter1 in range(int_repeat_number + 1):
                product = counter1**2
                print("{0}² = {1}".format(counter1, product))
    except Exception:
        print("Invalid Input")

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
