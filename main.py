#!/usr/bin/python3

import sys
import urllib.request
import json
from datetime import datetime




def main(argv):
    request = urllib.request.Request('https://etherchain.org/api/statistics/price', headers={'User-Agent': 'Mozilla/5.0'})
    answer = urllib.request.urlopen(request).read()
    answer = json.loads(answer.decode('utf-8'))
    # price_per_hour = answer['data']
    # datetime.strptime('2017-03-07T22:25:27.000Z', '%Y-%m-%dT%H:%M:%S')

    price_per_hour = [{'time': datetime.strptime(p['time'], '%Y-%m-%dT%H:%M:%S.000Z'), 'usd': p['usd']} for p in answer['data']]
    print(price_per_hour)


if __name__ == '__main__':
    main(sys.argv[1:])