import boto3

def lambda_handler(event, context):
  client = boto3.client('ses', region_name='us-east-2')
  response = client.send_email(
    Source="njesusmercado@gmail.com",
    Destination={
      'ToAddresses': ["njesusmercado@gmail.com"]
    },
    Message={
      'Subject': {
        'Data': event["subject"]
      },
      'Body': {
        'Text': {
          'Data': f"""
            {event["message"]}
            Sent by {event["name"]} at {event["email"]}
          """ 
        }
      }
    }
  )
  return response['MessageId']