#In Massachusetts it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones.
#Among the requirements, though, are:

  #“All vanity plates must start with at least two letters.”
  #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
  #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
  #“No periods, spaces, or punctuation marks are allowed.”
#In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all
#of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
#Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str.


def main():
    plate=input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    if 2 < len(s) > 6:  #Must contain a max of 6 char (letters or numbers) and a min of 2 characters.
        return False
    if s[0].isalpha==False and s[1].isalpha==False: #Must start with at least two letters.
        return False

    i=0
    while i < len(s): #The first number used cannot be a ‘0’.
        if s[i].isalpha==False:
            if s[i]==0:
                return False
            else:
                break
        i=i+1

    for i in range(len(s)):  #Numbers cannot be used in the middle of a plate.
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    for c in s:
        if c=='.' or c==' ' or c=='?' or c=='!':
            return False

    return True

main()

