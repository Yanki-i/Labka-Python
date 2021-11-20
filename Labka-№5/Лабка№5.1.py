import math
'''
Обчислити значення виразу
(1/2+cos(0.1))(2/3+cos(0.2))*...*(9/10+cos(0.9)).
'''
#Позначення
'''
a = чисельник - int
b = знаменник - int
c = косинус - float
'''
#Обчислення
a = 1
b = 2
c = 0.1
suma = (a/b + math.cos(c))
while a <= 9:
    suma = suma*(a/b + math.cos(c))
    a = a+1
    b = b+1
    c = c+0.1
print("Сума = {0}".format(suma))
