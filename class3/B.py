# Задача B. Сумма квадратов
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3531#1

n = int(input())
sum=0
for i in range(1,n+1):
    sum = sum + i**2
print(sum)
