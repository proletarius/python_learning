# Задача I. Диофантово уравнение - 1
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3542#1

a,b,c,d = int(input()), int(input()), int(input()), int(input())

for x in range(1001):
    if a * x**3 + b * x**2 + c * x + d == 0:
        print(x)
