# Задача G. Линейное уравнение
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3516#1

a,b = int(input()), int(input())
if (a == 0) and (b == 0):
    print('INF')
elif a != 0 and (b % a == 0):
    print(int(-b/a))
else:
    print('NO')
