#!/usr/bin/env python
import random
import sys
from pprint import pprint

class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if not self.is_empty():
            result = self.data[-1]
            self.data = self.data[0:-1]
            return result
        else:
            return False

    def size(self):
        return len(self.data)

    def show(self):
        print ", ".join(self.data)

class Rev(object):
    def __init__(self):
        self.count = 0

    def rev(self, s):
        self.count += 1
        if len(s) < 2:
            return s
        else:
            head, tail = s[0], s[1:]
            return self.rev(tail) + head

def class_rev(subject):
    r = Rev()
    print "{} = #{} chars".format(subject, len(subject))
    print r.rev(subject)
    print r.count


def stack_rev(subject):
    s = Stack()
    for letter in subject:
        s.push(letter)

    buf = []
    for i in xrange(s.size()):
        buf.append(s.pop())
    print "".join(buf)+"\0"






def main(subject):
    stack_rev(subject)



if __name__ == '__main__':
    subject = raw_input("Enter a string: ")
    print
    main(subject)



