#!/usr/bin/env python

def steps(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return steps(n-3) + steps(n-2) + steps(n-1)

def steps2(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return steps2(n-1) + steps2(n-2) + steps2(n-3)



if __name__ == '__main__':
    for n in range(1, 15):
        print "Steps: {}".format(n)
        print steps(n)

        print "Steps2: {}".format(n)
        print steps2(n)
        print '-------'


