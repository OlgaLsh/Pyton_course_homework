# выпуклый пятиугольник - расчет площади

from math import sqrt

a1 = (2, 3)
a2 = (1, 4)
a3 = (7, 5)
a4 = (7, 2)
a5 = (3, 4)


def one_side(a, b):
    side = sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]))
    return side


def tria_square(a, b, c):
    p = (a + b + c) / 2
    square = sqrt(p * (p - a) * (p - b) * (p - c))
    return square

firstside = one_side(a1, a2)
secondside = one_side(a2, a3)
thirdside = one_side(a3, a1)
print(firstside,secondside,thirdside)
fist_square = tria_square(firstside, secondside, thirdside)
print(fist_square)

firstside =thirdside
secondside = one_side(a3, a4)
thirdside = one_side(a4, a1)
print(firstside,secondside,thirdside)
second_square=tria_square(firstside, secondside, thirdside)
print(second_square)

firstside = thirdside
secondside = one_side(a4, a5)
thirdside = one_side(a5, a1)
print(firstside,secondside,thirdside)
third_square=tria_square(firstside, secondside, thirdside)
print(third_square)

figure_square=fist_square+second_square+third_square
print(figure_square)