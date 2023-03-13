#Implement a program that prompts the user for names, one per line, until the user inputs control-d.
#Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and,
#three names with two commas and one and, and "n" names with "n-1" commas and one and, as in the below:

    #Adieu, adieu, to Liesl
    #Adieu, adieu, to Liesl and Friedrich
    #Adieu, adieu, to Liesl, Friedrich, and Louisa
    #Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    #Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta

#pip install inflect (in command window)
import inflect
p = inflect.engine()
names=[] #Create a list to keep track of the names

while True:
    try:
        name=input('Name: ')
        names.append(name)  #To add the name to the list

    except EOFError:
        print()  #It will automatically print a new line
        break

output=p.join(names)
print('Adieu, adieu to ' + output)