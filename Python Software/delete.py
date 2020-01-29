from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "json.json"
prefix = 'himanshuchauhan981'+'/'+'29-09-2018'
print(prefix)
bucket_name = 'pyhton-project-6071.appspot.com'
client = storage.Client()
list1=[]
list2=[]
def list_blob_with_prefix(bucket_name,prefix,delimiter=None):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('pyhton-project-6071.appspot.com')
    blobs = bucket.list_blobs(prefix = prefix)
    print(blobs)
    for blob in blobs:
        b = str(blob.name).split(prefix+'/')[1]
        list1.append(b)
    print(list1)
list_blob_with_prefix(bucket_name,prefix)
