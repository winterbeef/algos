#!/usr/bin/env python
import sys

def proc(n):
    if n == 1:
        return 2
    else:
        return 2 * proc(n-1)

class Fibcalc():
    memo = {
        0: 0,
        1: 1,
    }

    def get(self, n):
        if n in Fibcalc.memo:
            print '(memo {})'.format(n)
            return Fibcalc.memo[n]
        else:
            print '(calc {})'.format(n)
            result = self.get(n-1) + self.get(n-2)
            Fibcalc.memo[n] = result
            return result

def fibtest():
    f = Fibcalc()
    fib100 = f.get(100)
    fib99 = f.get(99)
    print "{}, {}; ratio {}".format(fib100, fib99, float(fib100)/float(fib99))
    print Fibcalc.memo

def tricky(n):
    n = int(n)
    operations = 0
    while n > 0:
        for i in range(n):
            print("Operations: %d" % operations)
            operations += 1
        n = int(n/2)
    return n

def recursemult(a, b):
    a = int(a)
    b = int(b)

    if a==1:
        return b
    else:
        return b + recursemult(a-1, b)

def move(src, dst):
    print "Moved from {} to {}".format(src, dst)

def towers(sz, src, dst, tmp):
    sz = int(sz)
    if sz == 1:
        move(src, dst)
    else:
        towers(sz-1, src, tmp, dst)
        towers(1,    src, dst, tmp)
        towers(sz-1, tmp, dst, src)

LIMIT=1000
def fun2(n):
    n = int(n)
    if n <= 0:
        return
    if n > LIMIT:
        return

    print "+{}".format(n)
    fun2(2*n)
    print "-{}".format(n)



def main():
    testfun = sys.argv[1] if 1 < len(sys.argv) else 'fibtest'
    try:
        print globals()[testfun](*sys.argv[2:])
    except KeyError:
        print "No function called {}".format(testfun)

if __name__ == '__main__':
    # print sys.argv[2:]
    main()
