__author__ = 'Phil'
import urllib.request
import pickle

request = urllib.request.Request("http://www.pythonchallenge.com/pc/def/banner.p")

object = urllib.request.urlopen(request).read()
unpickled = pickle.loads(object)

print ("Unpickled:\n")

for object in unpickled:
    print(object)

out = ""
for object in unpickled:
    i = 0
    for part in object:
        key = part[0]
        value = part[1]
        out+=key*value
    print(out)
    out=""