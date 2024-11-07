import requests
from Config.settings import base_url,  DATA_FORMAT

class WorldBankModel:
    def fetch_data(country_code="all", date_range="2010:2020", INDICATORS ="SP.POP.TOTL" ):
        endpoint = f"{base_url}/country/{country_code}/indicator/{INDICATORS}"
        params = {
            "date": date_range,
            "format": DATA_FORMAT,
        }
        print(f"Fetching data from URL: {endpoint} with params: {params}") 
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if 'message' in data[0]: 
                print("API Error Message:", data[0]['message'])
                return None
            return data
        else:
            print(f"Error: Status code {response.status_code}")
            return None
