N = int(input())
l = []
for i in range(1, N + 1):
    st = input().split()

    if len(st) == 3:
        s = st[0]
        index = int(st[1])
        val = int(st[2])

    elif len(st) == 2:
        s = st[0]
        val = int(st[1])

    else:
        s = st[0]

    if s == 'insert':
        l.insert(index, val)

    elif s == 'remove':
        l.remove(val)

    elif s == 'append':
         l.append(val)

    elif s == 'print':
        print(l)

    elif s == 'pop':
        if len(l) > 0:
            l.pop()

    elif s == 'reverse':
        l.reverse()

    elif s == 'sort':
        l.sort()
