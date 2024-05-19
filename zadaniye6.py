# ============================================ №6*
# Имеется банковское API возвращающее JSON
# {
# 	"Columns": ["key1", "key2", "key3"],
# 	"Description": "Банковское API каких-то важных документов",
# 	"RowCount": 2,
# 	"Rows": [
# 		["value1", "value2", "value3"],
# 		["value4", "value5", "value6"]
# 	]
# }
# Основной интерес представляют значения полей "Columns" и "Rows",
# которые соответственно являются списком названий столбцов и значениями столбцов
#
# Задание:
# 	1. Получить JSON из внешнего API
# 		ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}
# 	2. Валидировать входящий JSON используя модель pydantic
# 		(из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
# 	2. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
# 	3. В полученном DataFrame произвести переименование полей по след. маппингу
# 		"key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
# 	3. Полученный DataFrame обогатить доп. столбцом:
# 		"load_dt" -> значение "сейчас"(датавремя)
#============================================================
# Реализация:
# потребуется испольховать сторонние библиотеки httpx, pydantic, pandas
# К сожалению не удалось подключиться к указанному API в задании (TimeoutError)
# В качестве тестовых данных был использован локальный API (api.py)

from datetime import datetime
from typing import List, Self
from urllib.parse import quote
import httpx
import pandas as pd
from pydantic import BaseModel, model_validator

REQ_PARAM = '{"начало дня сегодня в виде таймстемп"}'
URL_STR = "http://localhost:8000/very/important/docs?documents_date=" + quote(REQ_PARAM)

# req_param = '{"начало дня сегодня в виде таймстемп"}'
# url_str = "https://api.gazprombank.ru/very/important/docs?documents_date=" + quote(req_param)

# Модель валидации общей структуры JSON
class JSON_model(BaseModel):
    Columns: List[str]
    Description: str
    RowCount: int
    Rows: List[ List[int|datetime|str]]

    @model_validator(mode='after')
    def check_row_count(self) -> Self:
        if len(self.Rows) != self.RowCount:
            raise ValueError("Ошибка: RowCount не совпадает с количеством Rows")
        return self


# Модель валидации строк данных
class Rows_model(BaseModel):
    key1: List[int]
    key2: List[datetime]
    key3: List[str]


def parse_data(data: dict) -> bool:
    data = JSON_model(**data)
    rows = Rows_model(
        key1=[x[0] for x in data.Rows],
        key2=[x[1] for x in data.Rows],
        key3=[x[2] for x in data.Rows]
    )

    pd.set_option('display.max_columns', 5)
    df = pd.DataFrame(data=rows.dict())
    df.rename(columns={"key1": "document_id", "key2": "document_dt", "key3": "document_name"}, inplace=True)
    df["load_dt"] = datetime.now()

    print(df.head())

    return True

if __name__ == "__main__":
    try:
        with httpx.Client() as client:
            res = client.get(URL_STR,  follow_redirects=True, timeout=5)
            parse_data(res.json())
    except Exception as exp:
        print(f"Ошибка: {exp}")
