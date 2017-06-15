import time
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
from urllib.request import Request
def gethtml():
    url = Request("https://www.whatismypublicip.com/", headers={'User-Agent': 'Mozilla/5.0'})
    openurl = urllib.request.urlopen(url)
    content = str(openurl.read(5000000))
    soup = BeautifulSoup(content, "html.parser")
    good = soup.prettify()
    return good
def writefile():
    f = open('handle.txt', 'w')
    open('handle.txt', 'w').close()
    for lines in gethtml().split():
        string = str(lines)
        f.write(string)
        f.write(' \n ')
def IP():
    i = 0
    ip = None
    fh = open('handle.txt', 'r')
    for lines in fh.readlines():
        for word in lines.split():
            if i == 1:
                ip = word
                i = 0
            elif word == 'id="up_finished">':
                i = 1
    return ip
def where():
    i = 0
    co = None
    fh = open('handle.txt', 'r')
    for lines in fh.readlines():
        for word in lines.split():
            if word == 'Country:':
                i = 1
            elif i == 1:
                i = 2
            elif i == 2:
                i = 3
            elif i == 3:
                i = 4
            elif i == 4:
                co = word
                i = 0
    return co
p = 0
while (p < 10):
    writefile()
    print("YOUR PUBLIC IP IS: {} YOUR COUNTRY: {} ".format(IP(),where()))
    time.sleep(5)

