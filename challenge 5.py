__author__ = 'Phil'
import urllib.request
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

for i in range(0, 20000):
    pattern = re.compile('next nothing is [0-9]*')
    splitpattern = re.compile('\s')

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    #convert bytes to string
    response = response.read().decode("utf-8")
    response = pattern.findall(response)
    arrays = splitpattern.split(response[0])

    next = arrays[len(arrays)-1]
    if(next == '16044'):
        next = '8022'
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+next
    print(next)

