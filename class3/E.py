# Задача E. Пингвины
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3535#1

p1 = '   _~_    '
p2 = '  (o o)   '
p3 = ' /  V  \  '
p4 = '/(  _  )\ '
p5 = '  ^^ ^^   '

def drawPing(n):
    print(p1 * n)
    print(p2 * n)
    print(p3 * n)
    print(p4 * n)
    print(p5 * n)

n = int(input())
drawPing(n)