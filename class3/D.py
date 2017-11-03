# Задача D. Число сочетаний
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3534#1

def fac (x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
n, k = int(input()), int(input())
print(int(fac(n)/(fac(k)*fac(n-k))))