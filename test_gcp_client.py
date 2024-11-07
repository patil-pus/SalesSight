from Model.world_bank_model import fetch_data  


data = fetch_data('USA', "2010")

if data:
    print("Data successfully fetched!")
    print("Sample Data:", data[:4])
else:
    print("Failed to fetch data.")
