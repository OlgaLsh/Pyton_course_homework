# Заполнение списка размерностью m * n

m = int(input('Введите размерность m: '))
n = int(input('Введите размерность n: '))
x = 0
y = 1
arr = [[x * y for x in range(1, m+1)] for y in range(1, n+1)]
for row in arr:
    for i in row:
        print(i, end=' ')
    print()
