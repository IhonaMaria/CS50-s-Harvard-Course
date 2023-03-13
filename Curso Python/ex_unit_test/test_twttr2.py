#Assert keyboard is used when debugging a code.
#The assert keyboard lets you test if a condition in your code returns true. If not, it will raise an AssertionError


from twttr2 import shorten
def main(): #To call test functions
    test_upper_lower_case()
    test_numbers()


def test_upper_lower_case():  #Test letters upper and lower case
    assert shorten('twitter')=='twttr'
    assert shorten('TWITTER')=='TWTTR'
    assert shorten('TwIttER')=='TwttR'


def test_numbers():  #Test numbers
    assert shorten('1234')=='1234'

def punctuation(): #Test punctuation
    assert shorten('!?,:')=='!?,:'






