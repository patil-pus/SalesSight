from google.cloud import storage
import os 



def get_gcp_client():
    gcp_key_path = os.getenv('GCP_KEY_PATH')
    print(gcp_key_path)
    return storage.Client.from_service_account_json(gcp_key_path)

def fetch_gcp_files(bucket_name):
    client=get_gcp_client()
    bucket=client.bucket(bucket_name)
    return[blob.name for blob in bucket.list_blobs()]


    