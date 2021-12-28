a = [
      [3, 7, 1],
      [7, 1, 9],
      [5, 6, 2]
]
for i in range(len(a)):
        for j in range(len(a)+1):
            if a[i][j] != a[j][i]:
              print('Не симетрична')
            else:
              print('Симетрична')
            break