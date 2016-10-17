import requests


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
