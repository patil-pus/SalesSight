from Controller.data_ingestion_controller import DataIngestionController
import pandas as pd

class ViewController:
    def __init__(self, indicator=None):
        self.data_ingestion_controller=DataIngestionController(indicators=indicator)
        pass

    def prepare_dashboard_data(self,country_code='all',date_range='2010:2020'):
        combined_data=self.data_ingestion_controller.fetch_multiple_indicators(country_code=country_code,date_range=date_range)
        
        if combined_data is not None and not combined_data.empty:
            print('Data for dashboard is Ready:')
            return combined_data
        else:
            print('No data available')
            return pd.Dataframe()
