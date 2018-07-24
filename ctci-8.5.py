#!/usr/bin/env python
i = 0
hit = 0
memo = {}

def mult(m, n):
    global i, hit
    global memo
    i+=1

    (m, n) = min([m,n]), max([m,n])

    half = m //2
    rem = m - (half+half)

    if (m,n) in memo:
        hit += 1
        return memo[(m,n)]

    elif m == 2:
        memo[(2,n)] = n+n
        return memo[(2,n)]

    elif m == 1:
        memo[(1,n)] = n
        return memo[(1,n)]

    elif m == 0:
        return 0

    else:
        return mult(half, n) + mult(half, n) + mult(rem, n)



if __name__ == '__main__':
    tests = [
        (3, 7),
        (12, 5),
        (3, 3),
        (0, 3),
        (140, 12)

    ]

    for (m, n) in tests:
        print m, '*', n, '=',
        print mult(m,n)
        print
    print i, hit