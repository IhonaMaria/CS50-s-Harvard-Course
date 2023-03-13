#In a file called scourgify.py, implement a program that:

#Expects the user to provide two command-line arguments:
    #the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    #the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
#Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import sys
import csv

def command_line_arg():

    if len(sys.argv)<3:  #The user needs to provide exacly two-line command arguments
        sys.exit('Too few command-line arguments')
    if len(sys.argv)>3:
        sys.exit('Too many command-line arguments')
    #Check if it's a csv file:
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit('Not a CSV file')



if __name__ == "__main__":
    main()





