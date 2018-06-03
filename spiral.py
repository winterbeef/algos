#!/usr/bin/env python

import datetime
import pprint
import sys
import collections

directions = [
    ( 1,  0), # go east
    ( 0,  1), # go south
    (-1,  0), # go west
    ( 0, -1), # go north
]

def next_step(starts, deltas):
    return map(lambda start, delta: start + delta, starts, deltas)

def change_direction(cur_idx, directions):
    cur_idx = (cur_idx + 1) % len(directions)
    return directions[cur_idx]

def spiral(width):
    # spiral[0][0]       NW
    # spiral[n-1][n-1]   SE
    spiral = {
        k:{
            j:None for j in range(0, width)
        }
        for k in range(0, width)
    }

    x = -1
    y =  0
    dir_idx = 0
    deltas = directions[dir_idx]

    for step in range(0, width*width):
        (x1, y1) = next_step((x, y), deltas)

        if x1 in spiral and y1 in spiral[x1] and spiral[x1][y1] is None:
            spiral[x1][y1] = step

        else:
            deltas = change_direction(dir_idx, directions)
            (x1, y1) = next_step((x, y), deltas)
            spiral[x1][y1] = step

        (x, y) = (x1, y1)
    return spiral

if __name__ == '__main__':
    argv = collections.deque(sys.argv)
    prog = argv.popleft()
    width  = int(argv.popleft())

    print "Spiral of width {}".format(width)
    S = spiral(width)
    for y in range(0, width):
        for x in range(0, width):
            print "%3s" % (S[x][y],),
        print


