#!/usr/bin/env python
import random
from pprint import pprint

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "<{:02d}>".format(self.val)


def reverselist(head):
    if head is None:
        return None

    if head.next is None:
        return head

    last = head
    cur = head.next
    last.next = None

    while cur:
        next = cur.next
        cur.next = last
        last = cur
        cur = next

    head = last
    return head


def print_list(head):
    cur = head
    while cur:
        print cur,
        cur = cur.next
    print

def make_node():
    return Node(random.randint(0, 99))

def add_to_list(head, node):
    if head is None:
        node.next = head
        head = node

    elif head.val >= node.val:
        node.next = head
        head = node

    else:
        cur = head
        while cur.next and cur.next.val < node.val:
            cur = cur.next
        node.next = cur.next
        cur.next = node

    return head

def revprint(head):
    if head is None:
        print
        return
    revprint(head.next)
    print head,


if __name__ == '__main__':
    nodes = [make_node() for n in xrange(12)]
    head = make_node()

    for node in nodes:
        head = add_to_list(head, node)
    print_list(head)

    head = reverselist(head)
    print_list(head)

    # print " ".join([str(node) for node in nodes])
    # revprint(head)

