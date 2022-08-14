import json
from typing import Union


def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    """ Функция получения данных из JSON-файла"""

    with open(filename, encoding=encoding) as f:
        return json.load(f)
