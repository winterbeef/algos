


def fib(n):
    mem = [0, 1]
    n+=1
    # assume n > 1
    while len(mem) < n:
        mem.append(mem[-1] + mem[-2])

    print mem


for i in [5, 8, 1000, 3]:
    print '=========', i
    fib(i)
