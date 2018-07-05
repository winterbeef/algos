#!/usr/bin/env python

import datetime
import pprint

def fibber(n=20):
    a = 0
    b = 1
    yield(a)
    yield(b)
    counter = 2

    while True:
        counter += 1
        if counter > n:
            return
        yield(a+b)
        a, b = b, a+b

if __name__ == '__main__':
    gen = fibber(10)

    i = 0
    for num in gen:
        i += 1
        print "{:4d}\t{:6d}".format(i, num)




