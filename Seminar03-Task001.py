""" Задайте список из нескольких чисел. Напишите программу, которая
    найдёт сумму элементов списка, стоящих на нечётной позиции.
    Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12    """


def f(x):
    res = 0
    for i in range(1, len(x), 2):
        res += x[i]
    return res


lst, user_lst = [2, 3, 5, 9, 3], []

for digit in range(int(input('Количество чисел в списке: '))):
    user_lst.append(int(input(f'{digit+1} число: ')))

print(f'Список -> {lst}')
print(f'Сумма нечетных элементов списка: {f(lst)}')
print(f'Список -> {user_lst}')
print(f'Сумма нечетных элементов списка: {f(user_lst)}')
