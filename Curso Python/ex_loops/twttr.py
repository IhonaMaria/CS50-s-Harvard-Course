#When texting or tweeting, it’s common to shorten words to save time or space,
#as by omitting vowels, much like Twitter was originally called twttr.
#In a file called twttr.py, implement a program that prompts the user for a str of text
#and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

sentence=str(input('Input: '))
vocales=list('aeiou')
print('Output :', end='')

for char in sentence:
    if char in vocales:
        char=''
    print(char, end='')

print()