#!/usr/bin/env python

def magic(arr, lo, hi):
    if not arr:
        print "Empty"
        return False

    print "Lo {}, Hi {}".format(lo, hi)

    if lo == hi:
        if arr[hi] == hi:
            print "yay, @", hi
            return True
        else:
            print "boo..."
            return False
    else:
        mid = (hi + lo) // 2

        if arr[mid] == mid:
            print "yay, @", mid
        elif arr[mid] > mid:
            return magic(arr, lo, mid-1)
        else:
            return magic(arr, mid+1, hi)



if __name__ == '__main__':
    tests = [
        [-4, -3, -1, 0, 1, 3, 5],
        [-4,  0,  1, 2, 3, 5, 9],
        [-4, -3,  2, 4, 6, 9],
        [],

    ]

    for test in tests:
        print test
        magic(test, 0, len(test)-1)
        print
