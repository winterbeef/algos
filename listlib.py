#!/usr/bin/env python
import random

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
    return Node(random.randint(10, 80))

def new_list(sz):
    head = make_node()
    for i in xrange(sz-1):
        node = make_node()
        head.add_last(node)
    return head

if __name__ == '__main__':
    for sz in range(3, 6):
        l = new_list(sz)
        print_list(l)
        print
