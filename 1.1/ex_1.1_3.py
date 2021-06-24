# 3 exercise

name = input('Ваше имя: ')
sex = input('Ваш пол - М или Ж: ')
age = int(input('Ваш возраст: '))
if sex == "M":
    print(f'Его зовут {name}.Ему {age} лет')
else:
    print(f'Её зовут {name}.Ей {age} лет')