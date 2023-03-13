#Implement a program that:

#Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy.
#If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
#Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
#Be sure to catch any exceptions.
#Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.

import sys
import requests #Needed to take information from an API

#Helps on how to request from APIs:
#https://requests.readthedocs.io/en/latest/
#https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content


if len(sys.argv)==2:
    try:
        value=float(sys.argv[1]) #sys.argv[0] is already bitcoin.py, sys.argv[1] es lo que hay en la posición 1, que es el nombre n de bitcoins
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response=r.json()
    bitcoin=print(response['bpi']['USD']['rate_float'])  #In the dictionary, the price of bitcoins in dollars is in "rate" or "rate_flow".
              #It is in the dictionary BPI, and inside BPI in another dictionari called USD.
              #This gives the price ratio of 1 bitcoin in dollars.
    total_amount=bitcoin*value
    print(total_amount)
    
except requests.RequestException:
    print("RequestException")
    sys.exit()





