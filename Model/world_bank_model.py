import requests
from Config.settings import base_url, indicators, DATA_FORMAT

def fetch_data(country_code="all",date_range="2010:2020"):
    endpoint=f'{base_url}/country/{country_code}/indicator{';'.join(indicators)}'
    params={
        'date':date_range,
        'format':DATA_FORMAT,
    }
    response=requests.get(endpoint,params=params)
    print(response)
    return response.json() if response.status_code == 200 else None
