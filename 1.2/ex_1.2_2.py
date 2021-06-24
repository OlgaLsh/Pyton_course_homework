# Сумма цифр в строке
string = input('Введите буквы и цифры:')
a = 0
numbers = ['0','1','2','3','4','5','6','7','8','9']
for i in range(0, len(string)):
    if  str(string[i]) in numbers:
        a += int(string[i])
print('Сумма цифр: ')
print(a)