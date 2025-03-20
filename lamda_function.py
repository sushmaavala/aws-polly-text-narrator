import boto3

def lambda_handler(event, context):
    text = "Hello, this is a sample text being narrated using Amazon Polly."
    
    polly = boto3.client('polly')
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=text,
        VoiceId='Joanna'
    )
    
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='polly-storage1',
        Key='output.mp3',
        Body=response['AudioStream'].read()
    )
    
    return {
        'statusCode': 200,
        'body': 'Audio file created and uploaded to S3.'
    }
