#!/usr/bin/env python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "<{}>".format(self.data)

    def insert(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)

        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

class Q(object):
    from collections import deque

    def __init__(self, items):
        self.items = deque(items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.appendleft(item)

    def pop(self):
        return self.items.pop()


class Traverse(object):

    def __init__(self):
        self.level = 0
        self.items = []

    def inorder(self, node):
        self.level += 1
        if node.left:
            self.inorder(node.left)
        self.level -= 1

        print "{}\t{}".format(self.level, node.data)

        self.level += 1
        if node.right:
            self.inorder(node.right)
        self.level -= 1

    def inorder_items(self, node):
        self.level += 1
        if node.left:
            self.inorder_items(node.left)
        self.level -= 1

        self.items.append(dict(level=self.level, node=node))

        self.level += 1
        if node.right:
            self.inorder_items(node.right)
        self.level -= 1

    def fetch_items(self, node):
        self.items = []
        self.inorder_items(node)
        return self.items


class Bfs(object):

    def visit(self, node):
        print node.data


def maketree():
    import random
    def getrand():
        return int(random.randint(0,1000))

    root = Node(getrand())
    for i in xrange(int(1e2)):
        root.insert(getrand())

    return root

if __name__ == '__main__':
    root = maketree()

    trav = Traverse()
    # trav.inorder(root)
    items = trav.fetch_items(root)

    for n in items:
        print n
    print items






