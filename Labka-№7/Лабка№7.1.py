a = [
    [1, 4, 2],
    [3, 1, 5]
]
s = 0
for i in range(len(a)-1):
    for j in range(len(a)+1):
        s += a[i][j]
print('Sum={0}'.format(s))
