'''
Побудувати масив А=(ai), елементи якого задаються формулою
'''
b = float(input('b= '))
A = [b]
n = int(input('n= '))
a_i_2 = b
a_i_1 = b
suma = 0
i = 1
for i in range(3, n+1):
    a_i = a_i_2+a_i_1/2**a_i_1
    a_i_2 = a_i_1
    a_i_1 = a_i
    A.append(a_i)
while i < len(A):
    suma = suma+A[i]
    i = i+2
print(A)
print('Сума непарних елемантів з масиву A={0}'.format(suma))
