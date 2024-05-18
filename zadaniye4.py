# ============================================ №4
# # Имеется папка с файлами
# # Реализовать удаление файлов старше N дней

import datetime as dt
import os


def cleanup_files(location: str, N_days: int) -> bool:
    """Удаляет файлы в указанной директории старше N дней.
    Входные параметры:
    location: str - полный путь к директории (текущая директория - ".")
    N_days: int - количество дней
    """
    if type(location) != str or type(N_days) != int:
        print("Ошибка: Аргументы функции не валидны")
        return False
    date_limit = dt.datetime.now() - dt.timedelta(days=N_days)
    if not os.path.exists(location):
        print("Ошибка: Директория не найдена")
        return False
    try:
        prev_loc = os.getcwd()
        os.chdir(location)
        with os.scandir() as dir:
            for x in dir:
                if x.is_file() and dt.datetime. fromtimestamp(x.stat().st_mtime) < date_limit:
                    # print(x.name, " - ", dt.datetime. fromtimestamp(x.stat().st_mtime))
                    os.remove(x.name)
    except Exception as exp:
        print(f"Ошибка: {exp}")
        return False
    finally:
        if prev_loc:
            os.chdir(prev_loc)

    return True

if __name__ == "__main__":
    cleanup_files(".", 5)           # текущая директория, 5 дней