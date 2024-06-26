# ============================================ №5*
# В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
# Одна строка файла содержит одно слово.
#
# Задание:
# Написать программу которая выводит список слов,
# каждый элемент списка которого - это новое слово,
# которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
# Порядок вывода слов НЕ имеет значения
#
# Например, текстовый файл содержит слова:
# ласты
# стык
# стыковка
# баласт
# кабала
# карась
#
# Пользователь вводмт первое слово: ласты
# Программа выводит:
# ластык
# ластыковка
#
# Пользователь вводмт первое слово: кабала
# Программа выводит:
# кабаласты
# кабаласт
#
# Пользователь вводмт первое слово: стыковка
# Программа выводит:
# стыковкабала
# стыковкарась

#============================================================
# Реализация:



def get_words(file_name: str, depth: int = 1) -> bool:
    """
    Принимет введенное пользователем слово и выводит все совпадения по критерию:
    окончание введенного слова является началом слова из списка
    Входные параметры:
    file_name: str - файл содержащий список слов
    depth: int - минимальное количество совпадающих букв
    """
    data = []
    try:
        with open(file_name, "r", encoding="UTF-8") as file:
            for row in file:
                data.append(row.strip().lower())
    except Exception as exp:
        print(f"Ошибка: {exp}")

    word = input().strip().lower()

    for w in data:
        for indx in range(len(word)):
            if w.startswith(word[indx:]) and indx != 0 and indx + 1 >= depth:
                print(word + w.lstrip(word[indx:]))

    return True


if __name__ == "__main__":
    get_words("./data5.txt")