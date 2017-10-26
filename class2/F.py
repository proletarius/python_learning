# Задача F. Какое число больше?
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3502#1

a,b = int(input()), int(input())
if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)
