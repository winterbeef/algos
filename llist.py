#!/usr/bin/env python

from subprocess import call, check_output

class LinkedList(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None
        self.tail = None

    def __repr__(self):
        return '<List: %s>' % (self.show(),)

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return self

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        self.tail = node
        return self

    def show(self):
        buf = []
        node = self.head
        while True:
            if node:
                buf.append(node)
            else:
                break
            node = node.next
         return ' -> '.join([node.show() for node in buf])

class Node(object):
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.next = None

    def show(self):
        return "[%s]" % (str(self.data),)


if __name__ == '__main__':
    foo = check_output(['shuf', '-n5', '/usr/share/dict/words'])

    L = LinkedList()
    M = LinkedList()
    for word in foo.strip().split("\n"):
        M.append(Node(word))

    print M.show()

    print '--------'

    L.append(Node(4)).append(Node(5))
    print L.show()
    print '--------'

    L.append(Node('hella')).append(Node(77)).append(Node(M)).append(Node(8))
    print L.show()
    print '--------'
