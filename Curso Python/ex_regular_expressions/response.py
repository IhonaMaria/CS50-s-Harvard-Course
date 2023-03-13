#In a file called response.py, using either validator-collection or validators from PyPI, implement a program that prompts the user for an email address via input and then prints Valid or
#Invalid, respectively, if the input is a syntatically valid email address. You may not use re. And do not validate whether the email address’s domain name actually exists.


#In the codespace: pip install validator-collection

from validator_collection import validators

def main():
    email_adress=input("What's your email adress?")
    try:
        emailISValid=validators.email(email_adress)
        print('Valid')
    except:
        print('Invalid')



if __name__ == "__main__":
    main()
