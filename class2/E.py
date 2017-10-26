# Задача E. Максимум двух чисел
# http://informatics.mccme.ru/mod/statements/view3.php?id=16205&chapterid=3501#1

# вариант первый
#a = int(input("Введите число 1: "))
#b = int(input("Введите число 2: "))

#if a >= b:
#    print(a)
#else:
#    print(b)

# вариант второй
a,b = int(input()),int(input())
print(a if a >= b else b)
