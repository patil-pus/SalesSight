import os
from dotenv import load_dotenv

load_dotenv()

base_url= "https://api.worldbank.org/v2"

GOOGLE_CLOUD_BUCKET=os.getenv('GOOGLE-CLOUD-STORAGE')
print(GOOGLE_CLOUD_BUCKET)

DATA_FORMAT='json'

