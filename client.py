"""
Example client script to test server (assumed to be running locally at localhost:8090

Requests library required

Usage:
    $ python client.py
"""

import timeit
import json

import requests


def timer(fn):
    def timer_decorator(*args, **kwargs):
        start = timeit.default_timer()
        res = fn(*args, **kwargs)
        end = timeit.default_timer()
        print('Took %.2f seconds' % (end - start))
        return res
    return timer_decorator


@timer
def main():
    res = requests.get('http://localhost:8090/delay/5000', data=json.dumps({'ping': 'pong'}))
    print(res.text)


if __name__ == '__main__':
    main()
