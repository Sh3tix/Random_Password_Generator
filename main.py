from random import choice

"""
Author: G@b
Date: 12/04/2021
"""


# Generate alphabet with chr() function and for loop.
alphabet_upper = [chr(i) for i in range(65, 91)]
alphabet_lower = [chr(i) for i in range(97, 123)]
alphabet = alphabet_upper + alphabet_lower

# Generate numbers with for loop.
numbers = [str(i) for i in range(10)]

# Special list
special = ["!", "#", "%", "&", "(", ")", "{", "}", "[", "]", "-", "+", "*", "/", ".", ",", "^", "<", ">", ":", ";", "=",
           "?"]

password_len = int(input("Password length: "))
add_numbers = input("Add numbers (y/n): ")
add_special = input("Add special characters (y/n): ")

password = ""

for i in range(password_len):

    if len(password) < password_len:
        if add_special == "y":
            password += choice(special)

        if add_numbers == "y":
            password += choice(numbers)

        password += choice(alphabet)

print("Your password:", password)