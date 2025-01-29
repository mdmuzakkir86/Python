x = int(input())
y = int(input())
z = int(input())
n = int(input())

permutations = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(permutations)


even = [num for num in range(1, 11) if num%2 == 0]
print(even)