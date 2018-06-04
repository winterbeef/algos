#!/usr/bin/env python

import pprint

# [
#   {'digit': '2', 'count': '3'},
#
#
# ]




def str_to_obj(k):
    k = list(k)
    k.append(None)
    buf = []
    count = 0
    lastchar = k[0]

    for cur in k:
        if cur == lastchar:
            count += 1

        else:
            buf.append({
                'digit': lastchar,
                'count': count
            })
            count = 1
            lastchar = cur
    return buf

def obj_2_str(k):
    buf = []
    for entry in k:
        buf.append(str(entry['count']))
        buf.append(str(entry['digit']))
    return ''.join(buf)

if __name__ == '__main__':

    k = ''
    for i in range(12):
        m = str_to_obj(k)
        n = obj_2_str(m)
        print 'n =>', n
        k = n
