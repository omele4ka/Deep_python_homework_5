# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

FIRST_NUM = 0
SECOND_NUM = 1

def fibonacci_gen(n: int) -> list:
    a = FIRST_NUM
    b = SECOND_NUM
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*fibonacci_gen(10))