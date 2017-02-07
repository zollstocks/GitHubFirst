import requests
from calculus import *


def halloworld():
    print 'Hello World'
    print 'Hello Galaxy'
    print 'Was geht ab?'


def second():
    url = 'http://zollstocks.de'
    r = requests.get(url)
    print r
    print r.content

halloworld()
second()

print substract(3, 4)
print sum(4, 3)

class Car(object):

    wheels = 4

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def set_color(self, color):
        self.color = color


golf = Car('VW', 'Golf', 'blau')

print golf.wheels
print Car.wheels
print golf.color
golf.set_color('rot')
print golf.color
