# Задача F. Шоколадка
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3515#1

n,m,k = int(input()), int(input()), int(input())

if (k <= n * m) and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
