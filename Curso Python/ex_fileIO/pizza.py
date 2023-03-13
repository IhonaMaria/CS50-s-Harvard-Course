#Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
#and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
#Format the table using the library’s grid format. If the user does not specify exactly one command-line argument,
#or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

#pip install tabulate
import tabulate
import sys
import csv
from tabulate import tabulate

def main():
    command_line_arg()
    table=[]

    try:
        with open(sys.argv[1],"r") as csvfile:
            reader=csv.reader(csvfile)

        for row in reader:
            table.append(row)
        print(tabulate(table[1:],headers=table[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit('File does not exist')


def command_line_arg():

    if len(sys.argv)<2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv)>2:
        sys.exit('Too many command-line arguments')
    #Check if it's a csv file:
    if ".csv" not in sys.argv[1]:
        sys.exit('Not a CSV file')



if __name__ == "__main__":
    main()


