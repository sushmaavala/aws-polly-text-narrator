# Text Narrator using Amazon Polly (AWS Cloud Project)

This is a simple project where we convert a piece of text into speech using **Amazon Polly**. The output audio file is stored in an **Amazon S3** bucket using **AWS Lambda**.

## What this project does

- Converts text into an MP3 audio file using **Amazon Polly**
- Uploads the audio file to **Amazon S3** using a **Lambda function**
- Uses **IAM roles and permissions** to secure the process

## Files included

- `lambda_function.py`: Main code to convert text to speech and upload to S3
- `architecture-diagram.png`: Architecture diagram of the project


## Technologies Used

- AWS Lambda (Python)
- Amazon Polly
- Amazon S3
- AWS IAM (for roles and permissions)

## How it works

1. AWS Lambda triggers the code.
2. Amazon Polly converts text to speech.
3. The audio file is saved as `output.mp3`.
4. The file is uploaded to an S3 bucket.

## Cleanup Checklist

- Delete Lambda function
- Delete S3 bucket
- Delete IAM role & inline policies
- Delete IAM user (if created only for this project)
- Delete CloudWatch logs

## Result

You will find the MP3 file inside your **S3 bucket** after successful execution.

## Author

This project was created as a simple demo for learning AWS services and serverless application development.
