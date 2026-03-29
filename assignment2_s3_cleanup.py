import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')
BUCKET_NAME = "ankit-cleanup-bucket-123"

def lambda_handler(event, context):
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    for obj in response.get('Contents', []):
        if obj['LastModified'] < datetime.now(timezone.utc) - timedelta(minutes=1):
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])
            print(f"Deleted: {obj['Key']}")