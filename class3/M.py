# Задача M. Билеты на метро - 1
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3520#1

n = int(input())
a = 0
b = 0
c = 0
if n >= 60:
    c = n // 60
    n = n % 60
if n > (440 // 125)*10 + (440 - (440 // 125)*125) // 15:
    c = c+1
    n = 0
else:
    if n >=10:
        b = n // 10
        n = n % 10
if n > 125 // 15:
    b = b+1
else:
    a = n
print(a,b,c)
