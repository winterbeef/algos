#!/usr/bin/env python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


class Traverse(object):
    level = 0

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)

        print node.value

        if node.right:
            self.inorder(node.right)

if __name__ == '__main__':
    print 'Yay'

