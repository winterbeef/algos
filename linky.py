#!/usr/bin/env python
import random
from pprint import pprint

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "<{}>".format(self.val)


# class LinkedList(object):
#     def __init__(self, head=None):
#         self.head = head

#     def __repr__(self):
#         buf = []
#         node = self.head
#         while node:
#             buf.append(node)
#             node = node.next
#         return '->'.join([str(n) for n in buf])

def print_list(head):
    cur = head
    while cur:
        print cur,
        cur = cur.next

def make_node():
    return Node(random.randint(0, 100))

def add_to_list(head, node):
    if head is None:
        head = node
        return head

    elif head.val > node.val:
        node.next = head
        head = node
        return node

    else:
        cur = head
        while cur.next and cur.next.val < node.val:
            cur = cur.next
        node.next = cur.next
        cur.next = node




    return head

if __name__ == '__main__':
    nodes = [make_node() for n in xrange(12)]
    head = make_node()
    pprint(head)
    pprint(nodes)

    for node in nodes:
        add_to_list(head, node)

    print_list(head)

    # head = make_node()
    # node = make_node()

    # print "head -> {}, {}".format(id(head), head.val)
    # print "node -> {}, {}".format(id(node), node.val)

    # head = node

    # print "head -> {}, {}".format(id(head), head.val)
    # print "node -> {}, {}".format(id(node), node.val)



