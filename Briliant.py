n = int(input('Введіть позитивне непарне число: '))
if n % 2 == 0 or n <= 0:
    print('Помилка')
else:
    for i in range(n):
        if i < n // 2 + 1:
            print(" " * (n // 2 - i) + "*" * (2 * i + 1))
        else:
            print(" " * (i - n // 2) + "*" * (2 * (n - i) - 1))
