import requests

# ссылка на внешний источник (в нашем случае - ЦБ РФ)
url = 'https://www.cbr-xml-daily.ru/daily_json.js'

# получение списка доступных валют
def available_rates():
    result = {}
    try:
        response = requests.get(url).json()['Valute'].items()
        for k, v in response:
            result[k] = v['Name']
        result['RUB'] = 'Российский рубль'
        return result
    except Exception as e:
        return e

# конвертация из одной валюты в другую
def get_currency(from_, to, val):
    response = requests.get(url).json()['Valute']
    try:
        if from_ == 'RUB':
            valute_from = 1
        else:
            valute_from = response[from_]['Value']
        if to == 'RUB':
            valute_to = 1
        else:
            valute_to = response[to]['Value']
        return round((valute_from / valute_to * val), 2)
    except KeyError:
        return 'Некорректная пара валют. Доступные валюты по адресу: /available-rates'
