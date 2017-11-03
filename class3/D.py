# Задача D. Число сочетаний
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3534#1

n, k = int(input()), int(input())
n_fac = 1
k_fac = 1
nk_fac = 1
for i in range(1,n+1):
    n_fac = n_fac*i
for i in range(1, k+1):
    k_fac = k_fac*i
for i in range(1, (n-k)+1):
    nk_fac = nk_fac*i
print(int(n_fac/(k_fac*nk_fac)))