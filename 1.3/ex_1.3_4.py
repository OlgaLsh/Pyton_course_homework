# римские цифры в арабские

def latin_to_arab(number):
    numberlist = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                 (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = 0
    index = 0
    for arabic, latin in numberlist:
        while number[index: index + len(latin)] == latin:
            result += arabic
            index += len(latin)
    return result


number = input("Введите число римскими цифрами: ")
number = number.lstrip()
digit = latin_to_arab(number)
print(digit)
