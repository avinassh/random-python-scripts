import urllib
import urllib2
from time import sleep

def returnstr():
    return urllib2.urlopen('http://anonymouse.org/cgi-bin/anon-www.cgi/http://www.ign.com/private/prime/promo/infinity-blade-2-free/code').read()

for i in range(1, 500):
    string = returnstr()[returnstr().find('"code":')+8:returnstr().find('"res')]
    print string[:-2]
    sleep(2)