# 4 exercise
n = int(input('Введите число для расчёта факториала:'))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)
