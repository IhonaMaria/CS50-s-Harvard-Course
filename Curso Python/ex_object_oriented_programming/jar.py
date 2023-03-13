
# In a file called jar.py, implement a class called Jar

class Jar:
    def __init__(self, capacity=12):  #12 are the maximum cookies in the jar
        if capacity < 0:
            raise ValueError('Wrong capacity')
        self._capacity=capacity
        self._size=0 #we have no cookies at the beginning

    def __str__(self):
        return self._size * '🍪'

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError('Exceed capacity')
        if self._size + n > self.capacity:
            raise ValueError('Exceed capacity')
        self._size+=n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError('There are not enough cookies to remove')
        self._size-=n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


