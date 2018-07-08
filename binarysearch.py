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

def make_num():
    return random.randint(0, 99)

def make_node(n):
    return Node(n)

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

def binsearch(s, L, idx_left, idx_right):
    while idx_left <= idx_right:
        idx_mid = int((idx_left+idx_right)/2)
        print "[{}]=>{}".format(idx_mid, L[idx_mid])

        if L[idx_mid] == s:
            return idx_mid

        elif s < L[idx_mid]:
            idx_right = idx_mid - 1

        elif L[idx_mid] < s:
            idx_left = idx_mid + 1

        return binsearch(s, L, idx_left, idx_right)

    return False

def bs_iter(s, L):
    first = 0
    last = len(L) - 1

    while first <= last:
        mid = (first+last)//2
        if L[mid] == s:
            return mid
        elif s < L[mid]:
            last = mid-1
        elif L[mid] < s:
            first = mid + 1

    return False


if __name__ == '__main__':
    from pprint import pprint
    L = []
    for i in xrange(20):
        L.append(make_num())
    tests = L[1:3] + [make_num(), make_num(), max(L), min(L)]
    L.sort()
    print ", ".join(["[{:02d}] => {:02d}".format(i, l) for i, l in enumerate(L)])

    for i in tests:
        # result = binsearch(i, L, 0, len(L) - 1)
        result = bs_iter(i, L)
        if result is False:
            print "{} not found".format(i)
        else:
            print "{} found at {}".format(i, result)
