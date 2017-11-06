# Задача A. Четные индексы
# http://informatics.mccme.ru/mod/statements/view.php?id=16560#1

n = [int(x) for x in input().split()]
print(*n[::2], sep=' ')
