#Implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

#An IPv4 address is typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive.


import re #We'll use regular expressions to check if we are recieving the correct IPV format
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):  #r: is a raw string

        list_of_numbers=ip.split(".")
        for number in list_of_numbers:
            if int(number) < 0 or int(number) > 255:
                return False                                    # ^ and $ are to specify when to open and close
        return True                                             # One or more character between [0-9]
    else:
        return False                                            #  \. literally you expect a dot (.)
                                                                #regular expressions 101 website to test the expression
                                                                # We are testing in the ip variabe






if __name__ == "__main__":
    main()