# 5 exercise

def all_unique_numbers():
    number = 1000
    for i in range(number, 9999):
        number = number + 1
        k = str(number)
        if int(k[0]) != int(k[1]) and int(k[0]) != int(k[2]) and int(k[0]) != int(k[3]) and int(k[1]) != int(k[2]) and int(k[1]) != int(k[3]) and int(k[2]) != int(k[3]):
            print(k)


all_unique_numbers()