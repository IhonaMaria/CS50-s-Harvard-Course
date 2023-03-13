x=str(input('Camel Case: '))

for letter in x:
    if letter.isupper():
        print('_' + letter.lower(), end="")  #The end is to assure it'll be printed in the same line
    else:
        print(letter, end="")

print() #To delete the $ in the end

