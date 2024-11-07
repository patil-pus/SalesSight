import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apscheduler.schedulers.background import BackgroundScheduler
from Controller.view_controller import ViewController
import time

current_year=2010

def schedule_data_ingestion():
    global current_year
    view_controller=ViewController()
    data_range= f'{current_year}:{current_year}'
    data=view_controller.prepare_dashboard_data(country_code='all',date_range=data_range)

    if data:
        print(f'Data from year {current_year} fetched successfully')
    else:
        print(f'No data available for {current_year}')

    current_year +=1

def start_scheduler():

    scheduler=BackgroundScheduler()
    scheduler.add_job(schedule_data_ingestion,'interval',seconds=5)
    scheduler.start()
    print("Scheduler has been started. Data Ingestion would be running in every 5 Secs")

    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt,SystemExit):
        scheduler.shutdown()
        print('Scheduler Stopped')
        
if __name__=='__main__':
    start_scheduler()



