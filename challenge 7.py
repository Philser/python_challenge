__author__ = 'Phil'
import urllib.request
import zipfile
import re

zipurl = "http://www.pythonchallenge.com/pc/def/channel.zip"

dl = urllib.request.urlretrieve(zipurl, "dl.zip")
zip = zipfile.ZipFile("dl.zip", "r")

pattern = re.compile('Next nothing is [0-9]*')
splitpattern = re.compile('\s')

next = "80057.txt"

for i in range(0,1000):
    string = zip.open(next).read().decode('UTF-8')

    string = pattern.findall(string)
    arrays = splitpattern.split(string[0])

    next = arrays[len(arrays)-1]+".txt"
    comment = zip.getinfo(next).comment.decode('UTF-8')
    print(comment)

