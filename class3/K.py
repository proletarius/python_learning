# Задача K. Лесенка
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3547#1

n = int(input())
s = '1'
if n <= 9:
    print(s)
    for i in range(2,n+1):
        s = s + str(i)
        print(s)
