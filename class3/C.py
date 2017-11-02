# Задача C. Факториал
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3533#1

n = int(input())
fac = 1
for i in range(1,n+1):
    fac = fac*i
print(fac)