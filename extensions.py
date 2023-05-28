import json
import requests
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        # r = requests.get(f"https://api.exchangeratesapi.io/convert?to={base_key}&from={sym_key}")
        # resp = json.loads(r.content)
        # new_price = resp['rates'][sym_key] * amount
        # new_price = round(new_price, 3)
        # message = f"Цена {amount} {base} в {sym} : {new_price}"
        # return message
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_key}&from={sym_key}&amount={amount}"


        headers = {
            "apikey": "JSg7fimWUxdlHYZz1pN0WjmQGyxwfKJn"
        }

        response = requests.request("GET", url, headers=headers)

        status_code = response.status_code
        result = response.text
        return result

