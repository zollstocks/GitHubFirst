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

# ich verstehe halt nicht, warum dass hier nicht vernümpftig auf GutHub committed wird.

# test ob es jetzt entsprechend funktioniert

halloworld()
second()
