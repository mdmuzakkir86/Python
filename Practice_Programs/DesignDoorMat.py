# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print((i*'.|.').center(M, '-'))
# print('WELCOME'.center(M, '-'))
# for i in range(N-2, -1, -2):
#     print((i*'.|.').center(M, '-'))


n = 17
width = len(bin(n)[2:])
for i in range(1, n + 1):
    deci = str(i)
    octa = oct(i)[2:]
    hexa = hex(i)[2:].upper()
    bina = bin(i)[2:]

    print(deci.rjust(width), octa.rjust(width), hexa.rjust(width), bina.rjust(width))