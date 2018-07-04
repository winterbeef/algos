#!/usr/bin/env python

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


def main():
    f = Fibcalc()
    # for i in xrange(10):
    #     print
    #     print '{} => {}'.format(i, f.get(i))

    fib100 = f.get(100)
    fib99 = f.get(99)

    print "{}, {}; ratio {}".format(fib100, fib99, float(fib100)/float(fib99))

    print Fibcalc.memo

if __name__ == '__main__':
    main()
