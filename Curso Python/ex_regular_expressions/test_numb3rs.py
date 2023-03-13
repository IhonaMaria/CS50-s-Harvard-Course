from numb3rs import validate

def main():
    test_format()
    test_range()


def test_format():  #We are expecting to recieve #.#.#.#, four numbers
    assert validate(r'1.2.3.4')==True
    assert validate(r'1.2.3')==False
    assert validate(r'1.2.')==False
    assert validate(r'1.')==False

def test_range():
    assert validate(r'255.255.255.255')==True
    assert validate(r'1000.255.255.255')==False
    assert validate(r'255.1000.255.255')==False
    assert validate(r'255.255.1000.255')==False
    assert validate(r'255.255.255.1000')==False


#To do the test:
#cd ex_regular_expressions                          (first change the directory to where the two programs are)
#ex_regular_expressions/putest test_numb3rs.py
