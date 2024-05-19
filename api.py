# Данный модуль является дополнением к заданию № 6
# Может использоваться в качестве тестового API сервера тестовых данных
# Для работы модуля потребуется установить библиотеку FastAPI - pip install fastapi
# Запуск сервера осуществляется командой - uvicorn api:app --reload

from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

TEST_DATA = {
    "Columns": ["key1", "key2", "key3"],
    "Description": "Банковское API каких-то важных документов",
    "RowCount": 4,
    "Rows": [
        [1, datetime.fromisoformat("2024-05-18T18:14:21"), "value1.txt"],
        [2, datetime.fromisoformat("2024-05-18T18:14:21"), "value2.txt"],
        [3, datetime.fromisoformat("2024-05-18T18:14:21"), "value3.txt"],
        [4, datetime.fromisoformat("2024-05-18T18:14:21"), "value4.txt"]
    ]
}


@app.get("/very/important/docs")
async def read_data(documents_date: str):
    return TEST_DATA