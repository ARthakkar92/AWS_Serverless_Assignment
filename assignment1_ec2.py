import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ec2.describe_instances()

    stop_ids = []
    start_ids = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']

            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Action':
                    if tag['Value'] == 'Auto-Stop':
                        stop_ids.append(instance_id)
                    elif tag['Value'] == 'Auto-Start':
                        start_ids.append(instance_id)

    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print(f"Stopped: {stop_ids}")

    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print(f"Started: {start_ids}")
