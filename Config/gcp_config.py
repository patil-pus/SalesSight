from google.cloud import storage

def get_storage_client():
    return storage.Client()