#Implement a program that:

#Prompts the user for a level n. If the user does not input 1, 2, or 3, the program should prompt again.
#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
#digits. No need to support operations other than addition (+).
#Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
#the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
#The program should ultimately output the user’s score: the number of correct answers out of 10.
#Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    level=get_level()  #To store the level of the function below
    score=simulate_game(level)
    print("Score :", score)

def get_level():
    while True:
        try:
            level=int(input('Level: '))
            if level in [1,2,3]:
                break
        except:
            pass  #To prompt the user again

    return level


def generate_integer(level):
    if level==1:  #Number has to have 1 digit
        x=random.randint(0,9)
        y=random.randint(0,9)
    elif level==2: #Number has to have 2 digits
        x=random.randint(10,99)
        y=random.randint(10,99)
    else:
        x=random.randint(100,999)
        y=random.randint(100,999)
    return x,y

def simulate_round(x,y):
    count_tries=1
    while count_tries<=3:
        try:
            answer=int(input(f"{x}+{y}=")) #the f is used to dynamically insert the values of x and y into the string
                                      #t allows you to embed expressions inside string literals, using curly braces {}.
                                      # When the expression is evaluated, its result is inserted into the string.
            if answer==(x+y):
                return True
            else:
                count_tries+=1
                print('EEE')
        except:
            count_tries+=1
    print(f"{x}+{y}={x+y}")
    return False


def simulate_game(level):
    count_round=1
    score=0
    while count_round<=10:
        x,y=generate_integer(level)
        response=simulate_round(x,y)
        if response == True: #The user has answered correctly
            score=score+1
        count_round+=1
    return score


if __name__ == "__main__":
    main()

