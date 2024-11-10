from Model.world_bank_model import WorldBankModel

class DataIngestionController:
    def __init__(self, indicators=None):
        if indicators == None:
            self.indicators=["SP.POP.TOTL", "NY.GDP.MKTP.CD", "SI.POV.DDAY", "NY.GDP.PCAP.CD", "EG.USE.PCAP.KG.OE"]
        else:
            self.indicators=indicators
    
    def fetch_multiple_indicators(self,country_code="all", date_range="2010:2020"):
        combined_data=[]
        
        for INDICATORS in self.indicators:
            print(f'Fetching data from {INDICATORS}')
            data=WorldBankModel.fetch_data(country_code=country_code,date_range=date_range,INDICATORS=INDICATORS)
            
            if data:
                for record in data[1]:
                    record['indicator']=INDICATORS
                    combined_data.append(record)
            else:
                print('failed to fetch data')

        
        return combined_data

        
