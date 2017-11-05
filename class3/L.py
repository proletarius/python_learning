# Задача L. Упорядочить три числа
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3527#1

a, b, c = int(input()), int(input()), int(input())

if a > b:
    (a,b)=(b,a)
if b > c:
    (b,c)=(c,b)
if a > b:
    (a,b)=(b,a)
print(a,b,c)