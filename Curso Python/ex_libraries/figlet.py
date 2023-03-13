#Among the fonts supported by FIGlet are those at figlet.org/examples.html.
#FIGlet has since been ported to Python as a module called pyfiglet.    (pip install pyfiglet)!

#In a file called figlet.py, implement a program that:

#Expects zero or two command-line arguments:
    #Zero if the user would like to output text in a random font.
    #Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
#Prompts the user for a str of text.
#Outputs that text in the desired font.
#If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.


import sys #In order to expect zero or two command-line arguments.
import random
from pyfiglet import Figlet

figlet = Figlet()

#we are going to have 3 elements in our argv (the first is already $python figlet.py)
if len(sys.argv)==1:
    isRandomFont=True

elif len(sys.argv)==3 and (sys.argv[1]=='-f'or sys.argv[1]=='--font'):
    isRandomFont=False
else:
    print('Invalid usage')
    sys.exit(1)


#You can then get a list of available fonts with code like this:
figlet.getFonts()

if isRandomFont==False:
    try:
        figlet.setfont(font=argv[2])  #The position 2 is the name of the font
        print(figlet.renderText(msg))
    except:
        print('Invalid usage')
        sys.exit(1)

else:
    font=random.choice(figlet.getFonts())  #To print a random element from a list. We have to import random

msg=input('Input: ')
print('Output')
print(figlet.renderText(msg))





