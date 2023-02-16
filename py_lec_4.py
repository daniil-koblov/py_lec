# def f(x):
#     return x * x

# a = f
# print(a(5))
# ____________________

# def calk1(a):
#     return a + a

# def calk2(a):
#     return a * a

# def math(op, x):
#     print(op(x))

# math(calk2, 5)
# ____________________

# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk1, 5, 45)
# ____________________

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a, b: a + b

# math(calk1, 5, 45)
# ____________________

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a, b: a + b, 5, 45)
# --------------------

# ЗАДАЧА 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []

# for i in data:
#     if i % 2 == 0: 
#         res.append((i, i ** 2))
# print(res)
# ____________________

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x , x ** 2), res))
# print(res)
# ____________________

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x , x ** 2), res))
# print(res)
# ____________________

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x , x ** 2), res))
# print(res)
# ////////////////////

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)
# --------------------

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?
# data = '1 2 3 5 8 15 23 38'
# print(data)

# data = data.split()
# print(data)
# ____________________

# data = '1 2 3 5 8 15 23 38'
# print(data)

# data = list(map(int, data.split()))
# print(data)
# ////////////////////

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)
# ////////////////////

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)
# ____________________

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)
# ////////////////////

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) 
# ////////////////////

# colors = ['red', '885', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()
# ____________________

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')

# print(56)
# ____________________

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()
# ____________________

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()
# ////////////////////

# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
# ____________________

# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'
# ____________________

# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #
# 'main.py'
# ____________________

# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'
# ////////////////////

# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в
# файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
# должен указывать на директорию, а не на символическую ссылку.
