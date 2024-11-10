import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from apscheduler.schedulers.background import BackgroundScheduler
from Controller.view_controller import ViewController



current_year = 2010
scheduler = None
stop_scheduler_flag = False

def schedule_data_ingestion():
    global current_year, stop_scheduler_flag
    view_controller = ViewController()
    data_range = f'{current_year}:{current_year}'

    data = view_controller.prepare_dashboard_data(country_code='all', date_range=data_range)

    if data:
        print(f'Data from year {current_year} fetched successfully')
    else:
        print(f'No data available for {current_year}')

    if current_year >= 2023:
        print("Reached year 2023. Marking scheduler for shutdown.")
        stop_scheduler_flag = True
    current_year += 1

def start_scheduler():
    global scheduler, stop_scheduler_flag
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_data_ingestion, 'interval', seconds=1)
    scheduler.start()
    print("Scheduler has been started. Data Ingestion is running every second.")

    try:
        while True:
            if stop_scheduler_flag:
                print("Stopping scheduler...")
                scheduler.shutdown()
                break
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Scheduler Stopped')

if __name__ == '__main__':
    start_scheduler()
