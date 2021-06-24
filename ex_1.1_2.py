# 2 exercise

def leap_year(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print("Это не високосный год")
    else:
        print("Это високосный год")


your_year = input("Введите год: ")
year = int(your_year)
leap_year(year)