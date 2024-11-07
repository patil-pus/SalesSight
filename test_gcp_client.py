from Controller.view_controller import ViewController

indicators= ["SP.POP.TOTL", "NY.GDP.MKTP.CD", "SI.POV.DDAY", "NY.GDP.PCAP.CD", "EG.USE.PCAP.KG.OE"]

view_controller=ViewController(indicators)
result=view_controller.prepare_dashboard_data(date_range='2010:2020',country_code='all')

if result:
    print("Success")
    print('Sample Data', result[:3])
else:
    print('Unsuccessful')
# combined_data=[]



# for INDICATORS in indicators:
#     data = fetch_data('all','2010:2020',INDICATORS)
#     combined_data.append(data)


# if data:
#     print("Data successfully fetched!")
#     # print("Sample Data:", data)
# else:
#     print("Failed to fetch data.")

# print(combined_data)
