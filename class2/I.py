# Задача I. Максимум трех чисел
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3505#1

a,b,c = int(input()), int(input()), int(input())

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)
