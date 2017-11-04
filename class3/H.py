# Задача H. Коровы
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3517#1

n = int(input())

if n < 100:
    if ((n % 10 == 1) or (n == 1)) and (n != 11):
        print(str(n) + ' korova')
    elif (n % 10 in range(2,5)) and (n not in range(12,15)):
        print(str(n) + ' korovy')
    else:
        print(str(n) + ' korov')
