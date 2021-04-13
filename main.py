from random import choice
from sys import exit
import argparse

"""
Author: G@b
Date: 12/04/2021
"""


def get_args():
    parser = argparse.ArgumentParser(description="Random password generator")
    parser.add_argument("-l", "--length", type=int, dest="length", help="Length of the password (max 30)")
    parser.add_argument("-s", "--specials", action="store_true", help="Add specials characters")
    parser.add_argument("-n", "--numbers", action="store_true", help="Add numbers")

    return parser.parse_args()


def generate_password(password_len, add_numbers, add_special):
    password = ""
    if add_special == "y":
        add_special = True

    if add_numbers == "y":
        add_numbers = True

    # Generate alphabet with chr() function and for loop.
    alphabet_upper = [chr(i) for i in range(65, 91)]
    alphabet_lower = [chr(i) for i in range(97, 123)]
    alphabet = alphabet_upper + alphabet_lower

    # Generate numbers with for loop.
    numbers = [str(i) for i in range(10)]

    # Special list
    special = ["!", "#", "%", "&", "(", ")", "{", "}", "[", "]", "-", "+", "*", "/", ".", ",", "^", "<", ">", ":", ";",
               "=",
               "?"]

    for i in range(password_len):

        if len(password) < password_len:
            if add_special:
                password += choice(special)

            if add_numbers:
                password += choice(numbers)

            password += choice(alphabet)

    return password


def main():
    args = get_args()

    if args.length is not None:
        password_len = args.length
        add_numbers = ""
        add_special = ""

        if password_len > 30:
            return "-1", "[-] The length of the password must be less than or equal to 30"

        if args.specials:
            add_special = "y"

        if args.numbers:
            add_numbers = "y"

        password = generate_password(password_len, add_numbers, add_special)

        return password

    else:
        try:
            password_len = int(input("Password length (max 30): "))

        except ValueError:

            return "-1", "[-] The length of the password must be of type int"

        add_numbers = input("Add numbers (y/n): ")
        add_special = input("Add special characters (y/n): ")

        if password_len > 30:
            return "-1", "[-] The length of the password must be less than or equal to 30"

        password = generate_password(password_len, add_numbers, add_special)

        return password


if "__main__" == __name__:
    password = main()
    if "-1" in password:
        print(password[1])

    else:
        print("Your password:", password)

