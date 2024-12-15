# app/services/aws_s3_service.py
import boto3

class AWSS3Service:
    def __init__(self, access_key: str, secret_key: str, bucket_name: str):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        self.bucket_name = bucket_name

    def download_file(self, file_name: str, dest_path: str):
        self.s3.download_file(self.bucket_name, file_name, dest_path)

    def upload_file(self, file_path: str, file_name: str):
        self.s3.upload_file(file_path, self.bucket_name, file_name)
