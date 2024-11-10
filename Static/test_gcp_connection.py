import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from Config.gcp_config import fetch_gcp_files
from dotenv import load_dotenv



load_dotenv()
print(os.getcwd)

if __name__ == '__main__': 
    bucket_name = 'sales_bucket12'
    files=fetch_gcp_files(bucket_name)
    print(f'Files with bucket name {bucket_name}:{files}')
