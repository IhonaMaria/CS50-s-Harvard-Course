#Implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file,
#excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py,
#or if the specified file does not exist, the program should instead exit via sys.exit.
#Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import sys
def main():
    command_line_arg()
    try:
        file=open(sys.argv[1],'r')
        lines=file.readlines()
    except FileNotFoundError:
        sys.exit('File does not exist')

    count_lines=0
    for line in lines:
        if check_comment_or_empty_line(line)==False:
            count_lines+=1
    print(count_lines)


def command_line_arg():
    #The program expects exacly one command-line argument!
    if len(sys.argv)<2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv)>2:
        sys.exit('Too many command-line arguments')
    #Check if it's a python file:
    if ".py" not in sys.argv[1]:
        sys.exit('Not a Python file')

def check_comment_or_empty_line(line)  #If it's true we're not gonna count this line
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):  #lstrip() to delete the first blank space
        return True
    return False


if __name__ == "__main__":
    main()
