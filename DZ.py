#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в
# массиве A[1..N]. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны
# N целыхчисел Ai. Последняя строка содержит число X

# n = int(input('Введите размер элементов списка: '))
# a = [i for i in range(1, n + 1)]
# print (a)
# x = int (input('Введите число х: '))
# count = 0
# for i in range(n):
#     if a[i] == x:
#         count += 1
# print(f'Число {x} встречается в списке {count} раз.')



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# N = int(input())
# A = [i for i in range(1, N + 1)]
# print(*A)
# X = int(input())
# min = abs(X - A[0])
# num = A[0]
# for i in range(1, len(A)):
#     if abs(X - A[i]) < min and A[i] != X:
#            min = abs(X - A[i])
#            num = A[i]
# print(num)



# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.


# x = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
# a = input("Введите слово: ").upper()
# count = 0

# for i in a:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
#         for y in x:
#             if i in x[y]:
#                 count += y
# print(count)