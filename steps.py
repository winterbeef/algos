


def numways(n):
    mem = [1, 1, 2, 4]
    if n < len(mem):
        return mem[n]

    i = 3
    while i < n:
        i += 1
        mem.append(mem[i-1] + mem[i-2] + mem[i-3])

    return mem[n]

for i in [1, 2, 4, 5]:
    print '=========', i
    print numways(i)
