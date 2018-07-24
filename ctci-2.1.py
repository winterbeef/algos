#!/usr/bin/env python
import random
from pprint import pprint

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
    return Node(random.randint(1, 4))

def add_front(head, node):
    node.next = head
    return node # New head

def remove_dupes(head):
    seen = {}
    prev = None
    cur = head

    while cur:
        if cur.val in seen:
            prev.next = cur.next
        else:
            seen[cur.val] = True
            prev = cur
        cur = cur.next


if __name__ == '__main__':
    head = make_node()
    print 'head:', head

    for i in xrange(0):
        node = make_node()
        head.add_last(node)

    print_list(head)
    remove_dupes(head)
    print_list(head)

