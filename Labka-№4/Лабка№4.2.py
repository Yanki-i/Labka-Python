'''
Дано дійсні числа a, b, c. Знайти суму тих
з них, які належать інтервалу [x,y].
'''
#Позначення
'''
a-Перше число f
b-Друге число f
c-Трете число f
'''
#Введення
a = float(input('Введіть перше число : '))
b = float(input('Введіть друге число : '))
c = float(input('Введіть трете число : '))
x = float(input('Координата x: '))
y = float(input('Координата y: '))
#Порівння властивостей
suma = 0
if x <= a <= y:
    suma += a
elif x <= b <= y:
    suma += b
elif x <= c <= y:
    suma += c
print('Sum={0}'.format(suma))