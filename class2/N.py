# Задача N. Ход коня
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3513#1

x1,y1 = int(input()), int(input())
x2,y2 = int(input()), int(input())

horse_steps = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
if (x1 and y1 and x2 and y2) in range(1, 9):
    print('YES' if (x2-x1, y2-y1) in horse_steps else 'NO')