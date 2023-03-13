from jar import Jar


def test_init():
    jar=Jar() #We are creating the object
    assert jar.capacity==12

    jar2=Jar(3)  #We create another object with 3 capacity
    assert jar2.capacity==3



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(6)
    assert jar.size==6

    jar.deposit(3)
    assert jar.size==9   #The deposit is 6+3


def test_withdraw():
    jar=Jar()
    jar.deposit(6)
    jar.withdraw(3)

    assert jar.size==3  #6 from the diposit and we take 3 cookies, the size remains 3

    jar.withdraw(1)   #If we take another cookie....
    assert jar.size==2
