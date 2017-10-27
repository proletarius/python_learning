# Задача K. Ход ладьи
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3509#1

x1,y1 = int(input()), int(input())
x2,y2 = int(input()), int(input())

if (x1 and y1 and x2 and y2) in range(1, 9):
    if (x1 == x2) or (y1 == y2):
        print('YES')
    else:
        print('NO')