# Максим Мусулезный 15.07.2023
# Создайте функцию генератор чисел Фибоначчи.
# Вариант 1
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Вариант 2

def fib(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(*(fib(10)))