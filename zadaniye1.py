# ============================================ №1
# # имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# # пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)
#
# """
# lastname|name|patronymic|date_of_birth|id
# Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
# Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
# ...
# """
#
# # Задание
# # 1. Реализовать сбор уникальных записей
# # 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи

#============================================================
# Реализация:

# В задании отсутствуют требования к конечному виду обработанных данных
# Предпочту использовать словари в решении данной задачи
# Ключем словаря является id записи
# Значением по этому ключу является словарь с оставшимися полями записи
# В случае не уникальных записей - значением является список словарей

# Ниже закомментировано решение с использованием списков
# в случае если предполагался иной формат обработанных данных

import csv


def process_data(file: str, sep: str = "|") -> tuple:
    unique_records = {}
    non_unique_records = {}
    with open(file, mode='r', encoding="UTF-8") as csv_file:
        data = csv.reader(csv_file, delimiter=sep)
        head = [x.strip() for x in next(data)]
        head.pop()
        for record in data:
            record = [x.strip() for x in record]
            id = record.pop()
            if id in non_unique_records:
                non_unique_records[id].append(dict(zip(head, record)))
            elif id in unique_records:
                non_unique_records.setdefault(id, [unique_records.pop(id)])
                non_unique_records[id].append(dict(zip(head, record)))
            else:
                unique_records.setdefault(id, dict(zip(head, record)))
    return unique_records, non_unique_records


# Пример обработанных данных:
# unique_records
# {
# 	'312040348-3048': {'lastname': 'Фамилия1', 'name': 'Имя1', 'patronymic': 'Отчество1', 'date_of_birth': '21.11.1998'},
# 	'457865234-3472': {'lastname': 'Фамилия3', 'name': 'Имя3', 'patronymic': 'Отчество3', 'date_of_birth': '12.02.1985'}
# }
# non_unique_records
# {
# 	'457865234-3431': [
# 		{'lastname': 'Фамилия2', 'name': 'Имя2', 'patronymic': 'Отчество2', 'date_of_birth': '11.01.1972'},
# 		{'lastname': 'Фамилия4', 'name': 'Имя4', 'patronymic': 'Отчество4', 'date_of_birth': '11.01.1992'},
# 		{'lastname': 'Фамилия5', 'name': 'Имя5', 'patronymic': 'Отчество5', 'date_of_birth': '11.01.1992'}
# 		]
# }


if __name__ == "__main__":
    print(process_data("data1.csv"))


#============================================================
# Реализация ввиде списков:
# Каждый набор обработанных данных unique_records и non_unique_records список с заголовком
# и списки данных


# def process_data(file: str, sep: str = "|") -> tuple:
#     unique_records = []
#     non_unique_records = []
#     with open(file, mode='r', encoding="UTF-8") as csv_file:
#         data = csv.reader(csv_file, delimiter=sep)
#         head = [x.strip() for x in next(data)]
#         unique_records.append(head)
#         non_unique_records.append(head)
#         for record in data:
#             record = [x.strip() for x in record]
#             if any(True for x in non_unique_records if x[-1] == record[-1]):
#                 non_unique_records.append(record)
#                 continue
#             for i, u_record in enumerate(unique_records):
#                 if record[-1] == u_record[-1]:
#                     non_unique_records.append(unique_records.pop(i))
#                     non_unique_records.append(record)
#                     break
#             else:
#                 unique_records.append(record)
#     return unique_records, non_unique_records


# Пример обработанных данных:
# unique_records
# [
# 	['lastname', 'name', 'patronymic', 'date_of_birth', 'id'],
# 	['Фамилия1', 'Имя1', 'Отчество1', '21.11.1998', '312040348-3048'],
# 	['Фамилия3', 'Имя3', 'Отчество3', '12.02.1985', '457865234-3472']
# ]
# non_unique_records
# [
# 	['lastname', 'name', 'patronymic', 'date_of_birth', 'id'],
# 	['Фамилия2', 'Имя2', 'Отчество2', '11.01.1972', '457865234-3431'],
# 	['Фамилия4', 'Имя4', 'Отчество4', '11.01.1992', '457865234-3431'],
# 	['Фамилия5', 'Имя5', 'Отчество5', '11.01.1992', '457865234-3431']
# ]