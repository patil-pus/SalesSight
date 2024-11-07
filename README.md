# SalesSight
SalesSight is a data ingestion and analytics platform that fetches data from the World Bank API, processes it, and prepares it for dashboard visualization. The platform integrates with Google Cloud Storage (GCP) and Snowflake to store, process, and model data efficiently. It also features a scheduler to automate data ingestion at specified intervals.

Installation and Setup
Prerequisites
Python (version 3.8 or later recommended)
Google Cloud CLI (for GCP authentication)
Snowflake Account (for storing and analyzing data)
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/SalesSight.git
cd SalesSight
2. Set Up Virtual Environment and Install Dependencies
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
# On Windows:
venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate
Install required libraries:

bash
Copy code
pip install requests google-cloud-storage pandas python-dotenv apscheduler snowflake-connector-python
pip install gcloud
3. Configure Google Cloud Authentication
Install Google Cloud CLI: If you haven’t installed it yet, download and install it from the Google Cloud CLI page (for Windows users).
Authenticate: Log in to your Google Cloud account using the following command:
bash
Copy code
gcloud auth application-default login
4. Set Up Environment Variables
Create a .env file in the root directory and add the following environment variables for GCP and Snowflake access:

Google Cloud
plaintext
Copy code
GCP_KEY_PATH="path/to/your-service-account-key.json"
BUCKET_NAME="your_bucket_name"
Snowflake Configuration
plaintext
Copy code
SNOWFLAKE_ACCOUNT="your_snowflake_account"
SNOWFLAKE_USER="your_snowflake_user"
SNOWFLAKE_PASSWORD="your_password"
SNOWFLAKE_DATABASE="your_database"
SNOWFLAKE_SCHEMA="your_schema"
Project Structure
plaintext
Copy code
SalesSight/
├── Config/
│   ├── __init__.py
│   ├── gcp_config.py              # GCP configuration for accessing Google Cloud Storage
│   └── settings.py                # Environment variable configuration
├── Controller/
│   ├── __init__.py
│   ├── data_ingestion_controller.py # Controller to handle data ingestion from GCP to Snowflake
│   └── view_controller.py          # Prepares data for dashboard visualization
├── Model/
│   ├── __init__.py
│   └── world_bank_model.py         # Fetches data from World Bank API
├── Scripts/
│   ├── ingest_data.py              # Script to trigger data ingestion manually
│   └── scheduler.py                # Scheduler script to automate data ingestion
├── .env                            # Environment variables (not in version control)
├── README.md                       # Project documentation
Usage
1. Running the Scheduler
The scheduler automates data ingestion by fetching data for each year, starting from 2010, and incrementing the year with each run. The scheduler fetches data every minute by default.

To start the scheduler:

bash
Copy code
python Scripts/scheduler.py
2. Manual Data Ingestion
You can manually trigger data ingestion without the scheduler by running ingest_data.py:

bash
Copy code
python Scripts/ingest_data.py
Additional Notes
Setting Up Google Cloud
Ensure that you have configured your Google Cloud project correctly, including the necessary IAM permissions for the service account used in GCP_KEY_PATH.

Scheduler Configuration
The scheduler is currently set to run every minute, incrementing the year each time. You can adjust this interval or starting year by editing the scheduler.py script in the Scripts directory.