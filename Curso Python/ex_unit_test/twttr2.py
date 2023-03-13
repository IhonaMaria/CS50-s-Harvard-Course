# Reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten
#expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
#Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly,
#each of whose names should begin with test_ so that you can execute your tests with:


def main():
    message=str(input('Input: '))
    message_without_vowels=shorten(message)
    print('Output: '+ message_without_vowels)


def shorten(word):  #We need to create a function with a return in order to test it afterwords
    word_without_vowels=''
    for letter in word:
        if not letter.lower() in ['a','e','i','o','u']: #Pasamos la letra a minuscula y comprobamos si coincide con alguna vocal
            word_without_vowels+=letter
    return word_without_vowels


if __name__ == "__main__":
    main()


