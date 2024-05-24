import requests


if __name__ == '__main__':
    payload = {
                'lang': 'ru',
                'T': '',
                'q': '',
                'M': '',
                'n': '',
    }
    for point in ['Sheremetyevo', 'London', 'Cherepovec']:
        url = f'https://wttr.in/{point}'
        response = requests.get(url, params=payload)
        try:
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.HTTPError:
            print(f'Response for {point} failed')
            print(f'Status code: {response.status_code}')

