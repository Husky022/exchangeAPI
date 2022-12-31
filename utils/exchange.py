import requests

# ссылка на внешний источник (в нашем случае - ЦБ РФ)
url = 'https://www.cbr-xml-daily.ru/daily_json.js'

# получение списка доступных валют
def available_rates():
    result = {}
    valute_dict = {}
    try:
        response = requests.get(url).json()['Valute'].items()
        for k, v in response:
            valute_dict[k] = v['Name']
        valute_dict['RUB'] = 'Российский рубль'
        result['status'] = 'OK'
        result['body'] = valute_dict
        return result
    except Exception:
        result['status'] = 'Error'
        result['message'] = 'Ошибка при работе сервиса, повторите попытку позже.'
        return result

# конвертация из одной валюты в другую
def get_currency(sale, buy, quantity):
    result = {}
    try:
        response = requests.get(url).json()['Valute']
        try:
            if sale == 'RUB':
                valute_from = 1
            else:
                valute_from = response[sale]['Value']
            if buy == 'RUB':
                valute_to = 1
            else:
                valute_to = response[buy]['Value']
            result['status'] = 'OK'
            result['body'] = round((valute_from / valute_to * quantity), 2)
            return result
        except KeyError:
            result['status'] = 'Error'
            result['message'] = 'Некорректная пара валют. Доступные валюты по адресу: /available-rates'
            return result
    except Exception:
        result['status'] = 'Error'
        result['message'] = 'Ошибка при работе сервиса, повторите попытку позже.'
        return result

