import math


# метод половинного деления
def DichotomyMethod(f, a_start, b_start, eps):
    #Инициализируем переменные
    a = a_start
    b = b_start
    delta = eps / 2
    interval_length = b - a
    iters = 0
    function_calcs = 0
    while interval_length > eps: #Основной цикл, проверка на точность
        #находим точки делящие отрезок пополам
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        if f(x1) > f(x2):#Высчитвыаем, в какой стороне значение функции меньше
            a = x1
        else:
            b = x2
        interval_length = b - a
        function_calcs += 2
        iters += 1
    return (a + b) / 2.0, function_calcs, iters


# метод золотого сечения
def GoldenSectionMethod(f, a_start, b_start, eps):
    a = a_start
    b = b_start
    interval_length = b - a
    #Расчёт залотого сечения
    goldSec1 = (3 - math.sqrt(5)) / 2
    goldSec2 = (math.sqrt(5) - 1) / 2
    #Отступаем на золотое сечение с каждой стороны отрезка
    x1 = a + goldSec1 * interval_length
    x2 = a + goldSec2 * interval_length
    y1 = f(x1)
    y2 = f(x2)
    iters = 0
    function_calcs = 2
    while interval_length > eps: #Основной цикл, проверка на точность
        #Смотрим, с какой стороны функция меньше
        if y1 > y2:
            a = x1
            x1 = x2
            x2 = a + goldSec2 * (b - a)
            y1 = y2
            y2 = f(x2)
            function_calcs += 1
        else:
            b = x2
            x2 = x1
            x1 = a + goldSec1 * (b - a)
            y2 = y1
            y1 = f(x1)
            function_calcs += 1
        interval_length = b - a
        iters += 1
    return (a + b) / 2.0, function_calcs, iters


# метод Фибоначчи
def FibonacciMethod(f, a, b, eps):
    n1 = 1
    n2 = 1
    function_calcs = 0
    iters = 0
    while (b - a) > eps: #Основной цикл, проверка на точность
        i = 0
        #Вычисляем число Фибоначчи
        n = (b - a) / eps
        while i < n - 2:
            n_sum = n1 + n2
            n1 = n2
            n2 = n_sum
            i += 1
        #Расчитываем отрезки
        x1 = b - (n1 / n2) * (b - a)
        x2 = a + (n1 / n2) * (b - a)
        function_calcs += 2
        iters += 1
        #Сравниваем
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
    return (a + b) / 2.0, function_calcs, iters

#Функция
def f(x):
    return x * x * x - 12 * x - 5


# a0 = 0
# b0 = 2.5
# #Вызов методов
# print('Метод половинного деления -', end='')
# print(DichotomyMethod(f, a0, b0, 0.001))
# print("Метод золотого сечения -", end='')
# print(GoldenSectionMethod(f, a0, b0, 0.001))
# print("Метод Фибоначи - ", end='')
# print(FibonacciMethod(f, a0, b0, 0.01))
# print("Значения(Минитальное значение Y, Количество вычислений, Колличество итераций)")
