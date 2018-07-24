#!/usr/bin/env python

bad = [
    (6,3),
    (5,3),
    (4,2),
    (15,1),
    (3,2),
    (2,2),
    (1,1),
    (4,0)
]

tried = {}
i = 0

def pathto(x, y):
    global i
    global tried
    i += 1
    if (x, y) in bad or x < 0 or y < 0 or tried.get((x,y), None) == False:
        print "Failed {}, {}".format(x,y)
        tried[(x,y)] = False
        return False


    if x == 0 and y == 0:
        print "Fin!"
        return True
    elif tried.get((x-1,y), None) == False:
        if pathto(x, y-1):
            print "Going {}, {}".format(x,y)
            return True

    elif tried.get((x,y-1), None) == False:
        if pathto(x-1, y):
            print "Going {}, {}".format(x,y)
            return True

    elif pathto(x, y-1):
        tried[(x, y-1)] = True
        print "Going {}, {}".format(x,y)
        return True

    elif pathto(x-1, y):
        tried[(x-1, y)] = True
        print "Going {}, {}".format(x,y)
        return True

    else:
        return False

if __name__ == '__main__':
    pathto(16,4)
    print i
