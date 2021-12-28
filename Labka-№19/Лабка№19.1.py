with open('my.txt') as file:
    r = file.readline()
    a = int(r[0])+int(r[1])+int(r[2])/3
    s = 0
    for el in r:
        el = int(el)
        if el > a:
            s *= el
print('Добуток={0}', format(s))
