import requests
from time import sleep

URL = 'http://anonymouse.org/cgi-bin/anon-www.cgi/http://www.ign.com/private/prime/promo/modern-combat-4/code'

for i in range(1, 1000):
    r = requests.get(URL)
    print r.json()['code']
    sleep(2)