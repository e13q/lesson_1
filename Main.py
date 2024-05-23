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
        response = requests.get(url = f'https://wttr.in/{point}', params=payload) 
        try:
            response.raise_for_status()
            if response.ok:
                print(response.text)
        except requests.exceptions.HTTPError:
            print(f'Response for {point} failed. Status code: {response.status_code}') 