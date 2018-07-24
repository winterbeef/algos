#!/usr/bin/env python
import random
from pprint import pprint
from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "<{:02d}>".format(self.val)

    def add_last(self, new):
        cur = self
        while cur.next:
            cur = cur.next
        cur.next = new

def print_list(head):
    cur = head
    while cur:
        print cur,
        cur = cur.next
    print

def make_node():
    return Node(random.randint(1, 9))

def make_list(head, sz):
    for i in xrange(sz):
        node = make_node()
        head.add_last(node)


def kth(head, k):
    cur = head
    k += 1
    d = deque(maxlen=k)
    while cur:
        d.append(cur)
        cur = cur.next

    if len(d) == k:
        return d.popleft()
    else:
        return '-nope-'


if __name__ == '__main__':
    for sz in range(3, 6):
        print
        print "Size:", sz
        head = make_node()
        make_list(head, sz-1)
        print_list(head)

        for k in range(0, 5):
            print "Kth:", k,
            n = kth(head, k)
            print n 


