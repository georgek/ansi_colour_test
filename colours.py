#!/usr/bin/env python

import sys

# standard colour ranges
FG_RANGE = range(30, 38)
BG_RANGE = range(40, 48)
# bright colour ranges (nonstandard)
BFG_RANGE = range(90, 98)
BBG_RANGE = range(100, 108)

COLOURS = [
    "Black",
    "Red",
    "Green",
    "Yellow",
    "Blue",
    "Magenta",
    "Cyan",
    "White",
]


def ansi_code_wrap(string, codes):
    """Wraps string in given colour code"""
    code_string = ";".join(str(code) for code in codes)
    colour_sequence = f"\033[{code_string}m"
    reset_sequence = "\033[0m"
    return colour_sequence + string + reset_sequence


def main():
    print("Standard with background:")
    for fg_name, fg_code in zip(COLOURS, FG_RANGE):
        col_name = ansi_code_wrap(fg_name, [fg_code])
        sys.stdout.write(f"{col_name:<18}")

        for bg_name, bg_code in zip(COLOURS, BG_RANGE):
            col_name = ansi_code_wrap(fg_name, [fg_code, bg_code])
            sys.stdout.write(f"{col_name:<21}")

        sys.stdout.write("\n")

    print("Bold standard with background:")
    for fg_name, fg_code in zip(COLOURS, FG_RANGE):
        col_name = ansi_code_wrap(fg_name, [1, fg_code])
        sys.stdout.write(f"{col_name:<20}")

        for bg_name, bg_code in zip(COLOURS, BG_RANGE):
            col_name = ansi_code_wrap(fg_name, [1, fg_code, bg_code])
            sys.stdout.write(f"{col_name:<23}")

        sys.stdout.write("\n")

    print("Bright with background:")
    for fg_name, fg_code in zip(COLOURS, BFG_RANGE):
        col_name = ansi_code_wrap(fg_name, [fg_code])
        sys.stdout.write(f"{col_name:<18}")

        for bg_name, bg_code in zip(COLOURS, BG_RANGE):
            col_name = ansi_code_wrap(fg_name, [fg_code, bg_code])
            sys.stdout.write(f"{col_name:<21}")

        sys.stdout.write("\n")

    print("Bright with bright background:")
    for fg_name, fg_code in zip(COLOURS, BFG_RANGE):
        col_name = ansi_code_wrap(fg_name, [fg_code])
        sys.stdout.write(f"{col_name:<18}")

        for bg_name, bg_code in zip(COLOURS, BBG_RANGE):
            col_name = ansi_code_wrap(fg_name, [fg_code, bg_code])
            sys.stdout.write(f"{col_name:<22}")

        sys.stdout.write("\n")


if __name__ == '__main__':
    main()
