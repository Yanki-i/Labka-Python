'''
Дано одновимірний масив дійсних чисел X.
В цьому масиві поміняти місцями елементи, що розташовані симетрично відносно середини.
'''
a = list(map(int, input('Введіть декілька дійсних чисел: ').split()))
k = -1
for i in range(len(a)//2):
    print('\nбуло - ', i, a)
    a[k], a[i] = a[i], a[k]
    print('Стало    ', a)
    k -= 1
