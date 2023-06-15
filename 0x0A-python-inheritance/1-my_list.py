#!/usr/bin/python3

"""My list class Module"""

class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
         """sorted list Method"""

        print(sorted(list(self)))


