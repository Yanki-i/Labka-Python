import math
a = [
    [2,-1, 7, -8],
    [1, 2, -2, 7],
    [-5, -24, 2, 1],
    [-4, 2, -4, 1]
]
for i in range(0, len(a), 2):
    for j in range(len(a[i])):
        if a[i][j] < 0:
            t = a[i-1][j]
            a[i-1][j] = a[i][j]
            a[i][j] = t
print(a)
