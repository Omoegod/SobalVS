
a = int(input('Введите значение 1:'))
b = int(input('Введите значение 2:'))
c = int(input('Введите значение 3:'))

result = a and b and c and 'Нет нулевых значений!!!'
result2 = a and b and c or 'Введены все нули!'
print('Действие № 1: ' + str(result))
print('Действие № 2: ' + str(result2))

if a > b + c:
    print('Действие № 3: ' + str(a - b - c))
else:
    print('Действие № 4: ' + str(b + c - a))

if a > 50 and b > a or c > a:
    print('Действие № 5: ' + 'Вася')
else:
    pass    

if a > 5 or b == 7 or c == 7:
    print('Действие № 6: ' + 'Петя')
else:
    pass