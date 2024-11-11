import json
from Model.world_bank_model import WorldBankModel
from Config.gcp_config import upload_to_gcp
import pandas as pd

class DataIngestionController:
    def __init__(self, indicators=None):
        if indicators is None:
            self.indicators = ["SP.POP.TOTL", "NY.GDP.MKTP.CD", "SI.POV.DDAY", "NY.GDP.PCAP.CD", "EG.USE.PCAP.KG.OE"]
        else:
            self.indicators = indicators

    def fetch_multiple_indicators(self, country_code="all", date_range="2010:2020"):
        combined_data = []

        for indicator in self.indicators:
            print(f'Fetching data for indicator {indicator}')
            data = WorldBankModel.fetch_data(country_code=country_code, date_range=date_range, INDICATORS=indicator)

            if data and len(data) > 1: 
                for record in data[1]:
                    record['indicator'] = indicator
                    combined_data.append(record)
            else:
                print(f'Failed to fetch data for indicator {indicator}')

        df = pd.DataFrame(combined_data)
        if not df.empty:
            return df
        else:
            print("No valid data fetched.")
            return pd.DataFrame()

    def save_data_to_gcp(self, data, bucket_name, file_name):
        json_data = data.to_json(orient="records")
        upload_to_gcp(bucket_name, file_name, json_data)
