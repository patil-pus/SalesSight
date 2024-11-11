import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from apscheduler.schedulers.background import BackgroundScheduler
from Controller.view_controller import ViewController



current_year = 2010
scheduler = None
stop_scheduler_flag = False
is_job_running = False

def schedule_data_ingestion():
    global current_year, stop_scheduler_flag, is_job_running

    if is_job_running:
        print(f"Job skipped for year {current_year}: Previous job still running")
        return

    is_job_running = True
    print(f"Starting data ingestion for year {current_year}...")

    try:
        view_controller = ViewController()
        data_range = f'{current_year}:{current_year}'
        data = view_controller.prepare_dashboard_data(country_code='all', date_range=data_range)

        if data is not None and not data.empty:
            print(f'Data from year {current_year} fetched successfully.')
            bucket_name = os.getenv('GOOGLE_CLOUD_STORAGE')
            file_name = f"data_{current_year}.json"
            view_controller.data_ingestion_controller.save_data_to_gcp(data, bucket_name, file_name)
        else:
            print(f'No data available for year {current_year}.')

        if current_year >= 2023:
            print("Reached year 2023. Marking scheduler for shutdown.")
            stop_scheduler_flag = True

        current_year += 1
    except Exception as e:
        print(f"Error during data ingestion for year {current_year}: {e}")
    finally:
        is_job_running = False

def start_scheduler():
    global scheduler, stop_scheduler_flag

    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_data_ingestion, 'interval', seconds=5)
    scheduler.start()
    print("Scheduler has been started. Data Ingestion is running every 5 seconds.")

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
