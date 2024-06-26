# ============================================ №2
# # в наличии список множеств. внутри множества целые числа
# m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
#
# # Задание: посчитать
# #  1. общее количество чисел
# #  2. общую сумму чисел
# #  3. посчитать среднее значение
# #  4. собрать все множества в один кортеж
# # *написать решения в одну строку

#============================================================
# Реализация:

if __name__ == "__main__":
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

    print(f"1. общее количество чисел: {sum(1 for x in m for itm in x)}")
    print(f"2. общая сумма чисел: {sum(itm for x in m for itm in x)}")
    print(f"3. среднее значение: {sum(itm for x in m for itm in x) / sum(1 for x in m for itm in x)}")
    print(f"4. собрать все множества в один кортеж: {tuple(itm for x in m for itm in x)}")