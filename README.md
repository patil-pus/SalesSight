# SalesSight

SalesSight is a data ingestion and analytics platform that fetches data from the World Bank API, processes it, and prepares it for dashboard visualization. The platform integrates with Google Cloud Storage (GCP) and Snowflake to store, process, and model data efficiently. It also features a scheduler to automate data ingestion at specified intervals.

## Installation and Setup

### Prerequisites
- **Python** (version 3.8 or later recommended)
- **Google Cloud CLI** (for GCP authentication)
- **Snowflake Account** (for storing and analyzing data)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SalesSight.git
cd SalesSight


python -m venv venv
# On Windows:
venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate


pip install requests google-cloud-storage pandas python-dotenv apscheduler snowflake-connector-python
pip install gcloud


gcloud auth application-default login


GCP_KEY_PATH="path/to/your-service-account-key.json"
BUCKET_NAME="your_bucket_name"


SNOWFLAKE_ACCOUNT="your_snowflake_account"
SNOWFLAKE_USER="your_snowflake_user"
SNOWFLAKE_PASSWORD="your_password"
SNOWFLAKE_DATABASE="your_database"
SNOWFLAKE_SCHEMA="your_schema"


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


python Scripts/ingest_data.py



This is ready to be saved directly into a `README.md` file. Just copy this text and paste it into a new file named `README.md` in your project directory.

