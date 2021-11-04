'''
Дано два дійсних числа. Знайти суму, добуток,
середнє арифметичне та середнє геометричне цих чисел
'''
#Позначення
'''
Перше число f-first_number
Друге число f-second_number
'''
#Введення
first_number = float(input('Перше число: '))
second_number = float(input('Друге число: '))
#Обчислення
suma = first_number+second_number
mult = first_number*second_number
mean = first_number+second_number
mean = mean//2
geometric_mean = first_number*second_number
geometric_mean = geometric_mean**0.5
print('Сума: ', suma)
print('Добуток:', mult)
print('Середнє арефметичне:', mean)
print('Середнэ геометричне: {0:2f}'.format(geometric_mean))