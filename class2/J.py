# Задача J. Существует ли треугольник?
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3506#1


# вариант первый
#from math import sqrt
#a,b,c = int(input()), int(input()), int(input())
#p = (a+b+c)/2
#if sqrt(p*(p-a)*(p-b)*(p-c)) == 0:
#    print('NO')
#else:
#    print('YES')

# вариант второй
a,b,c = int(input()), int(input()), int(input())
d = max(a,b,c)
print('YES' if a+b+c > 2*d else 'NO')
