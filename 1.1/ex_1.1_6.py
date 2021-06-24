# 6 exercise

def prime_number():
    n = int(input('Задайте диапазон простых чисел: '))
    for i in range(1, int(n) + 1):
        for k in range(2, int(n)):
            if int(i) % int(k) != 0 and int(i) % 2 != 0:
                print(i)
                break


prime_number()
