#!/usr/bin/env python

from collections import deque
import pprint

class Q(object):
    def __init__(self, vals=[]):
        self.vals = deque(vals)

    def is_empty(self):
        return len(self.vals) == 0

    def enq(self, v):
        self.vals.appendleft(v)
        return self

    def deq(self):
        if self.is_empty():
            raise Q.Error("Whoops! Empty q.")

        return self.vals.pop()

    def showme(self):
        print ','.join([str(v) for v in list(self.vals)])

    class Error(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)


def test_vals():
    return [
        range(4),
        range(0),
        range(6, 21, 3),
        range(88, 4, -6),
    ]


if __name__ == '__main__':

    for v in test_vals():
        q = Q(v)
        q.showme()

    q = Q(test_vals()[3])

    for v in [1, 4, -9, 11]:
        try:
            q.showme()
            q.enq(v)
            print "Enq {}".format(v)
            q.showme()
            print

            for i in range(3):
                print "Deq!"
                print q.deq()
                q.showme()
                print

        except Exception as e:
            print "Error({0})".format(e.value)
