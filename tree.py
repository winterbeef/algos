#!/usr/bin/env python

from subprocess import check_output

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, node):
        if node.data <= self.data:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def inorder(self):
        if self.left:
            self.left.inorder()

        print self.data

        if self.right:
            self.right.inorder()


if __name__ == '__main__':
    from pprint import pprint
    foo = check_output(['shuf', '-n10', '/usr/share/dict/words'])
    words = foo.strip().split("\n")

    print '--------'

    root = Node('/')
    for word in words:
        root.insert(Node(word))

    root.inorder()

    print '--------'
