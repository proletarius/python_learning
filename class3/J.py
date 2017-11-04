# Задача J. Замечательные числа - 2
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3545#1

for i in range(100, 999):
    if int(str(i**2)[-3:]) == i:
        print(i)
