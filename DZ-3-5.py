# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci_1(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a - b

def fibonacci_2(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data_1 = list(fibonacci_1(8))
data_2 = list(fibonacci_2(9))
print(data_1 + data_2 )

