#!/usr/bin/env python
import listlib

def delmid(head):
    p1 = None
    p2 = head

    while p2:
        p2 = p2.next
        if p2:
            p1 = p1.next if p1 else head
            p2 = p2.next


    if p1 and p1.next and p1.next.next:
        p1.next = p1.next.next


if __name__ == '__main__':
    for sz in range(1, 9):
        l = listlib.new_list(sz)
        listlib.print_list(l)

        delmid(l)
        listlib.print_list(l)
        print


