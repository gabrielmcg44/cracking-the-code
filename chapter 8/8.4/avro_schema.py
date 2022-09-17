from google.cloud import storage
import sys
from avro.datafile import DataFileReader
from avro.io import DatumReader
import json

client = storage.Client()

bucket_name = sys.argv[1]
blob_name = sys.argv[2]
file_name = sys.argv[3]

bucket = client.lookup_bucket(bucket_name)
if bucket is None:
    raise ValueError('Could not find bucket %s' % bucket_name)

blob = bucket.blob(blob_name)

blob.download_to_filename(file_name, start=0, end=100000)

reader = DataFileReader(open(file_name, "rb"), DatumReader())

schema = reader.get_meta('avro.schema')

parsed = json.loads(schema)

print(json.dumps(parsed, indent=4, sort_keys=True))