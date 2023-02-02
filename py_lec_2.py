# Вторая лекция

#  Листы

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 = list()
# list_3 = [1, 2, 3, 8]
# print(list_1)
# print(list_2)

# print(len(list_3))

# print(list_3[0])
# print(list_3[-1])
# print(len(list_1)-1)

# print(*list_3)

# for i in list_1:
#     print(i)

# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)
# print(list_1.pop())
# print(list_1)

# a = list_1.pop()
# print(a)
# print(list_1.pop(3))
# print(list_1)

# print(list_1.insert(2, 14))
# print(list_1)

# print(list_1[:])
# print(list_1[:2])
# print(list_1[3:])
# print(list_1[len(list_1)-2:])
# print(list_1[2:9])
# print(list_1[6:-18])
# print(list_1[0:len(list_1):6])
# print(list_1[::6])


# Кортежи

# t = ()

# print(type(t))

# t = (1, 5, 3,)
# print(type(t))

# v = [1, 8, 9]
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a = 1
# b = 2
# a, b = 1, 2
# a = b = 1

# a,b,c = v
# print(a, b, c)

# t = (1, 2, 3, 5,)

# for i in t:
#     print(i) 

#      ИЛИ

# for i in range(len(t)):
#     print(t[i])

# t[0] = 2 - Это ошибка. Изменять кортеж нельзя.


# Словари

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# print(dictionary.items())

# for (k,v) in dictionary.items():
#     print(k, v)

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
    # или
    # print(f'{item}: {dictionary[item]}')

    # print(item)


# dictionary[895] = 98998
# print(dictionary)


# Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()
# q = set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} копирование 'a' в новую переменную 'c'
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение 'а' и 'b'
# i = a.intersection(b) # i = {8, 2, 5} сходство 'а' и 'b'
# dl = a.difference(b) # dl = {1, 3} отличие 'а' от 'b'
# dr = b.difference(a) # dr = {13, 21} отличие 'b' от 'a'
# q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} выполнение нахождения 'а' от 'b' и 'b' от 'a' через объединение 'а' и 'b'
# a = {1, 8, 6}

# b = frozenset(a)

# print(b)


# List Comprehension (генератор списка)

# # Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:

# 1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так с помощью генератора списка:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]

# SyntaxError(Синтаксическая ошибка)
number_first = 5
number_second = 7
if number_first > number_second # !!!!!
 print(number_first)
# Отсутствие :

# IndentationError(Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:
print(number_first) # !!!!!
# Отсутствие отступов

# TypeError(Типовая ошибка)
text = 'Python'
number = 5
print(text + number)
# Нельзя складывать строки и числа

# ZeroDivisionError(Деление на 0)
number_first = 5
number_second = 0
print(number_first // number_second)
# Делить на 0 нельзя

# KeyError(Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])
# Такого ключа не существует

# NameError(Ошибка имени переменной)
name = 'Ivan'
print(names)
# Переменной names не существует

#  ValueError(Ошибка значения)
text = 'Python'
print(int(text))
# Нельзя символы перевести в целые значения

