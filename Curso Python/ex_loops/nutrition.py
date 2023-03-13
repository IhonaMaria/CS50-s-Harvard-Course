#In a file called nutrition.py, implement a program that prompts consumers users to input a fruit
#and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits,
# which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

fruits={'Apple':'130','Banana':'110','Grapes':'90'}

fruit_asked=str(input('Item: '))
for fruita in fruits:
    if fruita==fruit_asked:
        print('Calories: ',fruits[fruita])
        





