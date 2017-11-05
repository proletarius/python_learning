# Задача N. Сумма факториалов
# http://informatics.mccme.ru/mod/statements/view3.php?id=16206&chapterid=3551#1

n = int(input())

def sum_fac(n):
    run_sum, total_sum = 1, 0
    for i in range(n):
        run_sum *= (i+1)
        total_sum += run_sum
    return total_sum
print(sum_fac(n))
