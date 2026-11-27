#!/usr/bin/python3
"""Print first x integer elements of a list, skipping non-integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integer elements in first x items; raise IndexError if x > len."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
