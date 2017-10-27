# Задача M. Високосный год
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3504#1

n = int(input())

if (n%4 == 0) and (n%100 != 0) or (n%400 == 0):
    print('YES')
else:
    print('NO')