# Задача H. Гипотенуза
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3455#1

from math import sqrt

a,b = int(input()), int(input())
if a < 1000 and b < 1000:
    print(sqrt(a ** 2 + b ** 2))
else:
    print("Введите числа меньше 1000!")
