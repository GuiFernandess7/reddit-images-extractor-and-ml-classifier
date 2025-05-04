import boto3
import logging


class S3DatabaseHandler:
    def __init__(self, bucket_name, db_file_key):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name
        self.db_file_key = db_file_key

    def download_db(self, dest_path):
        try:
            self.s3.download_file(self.bucket_name, self.db_file_key, dest_path)
            logging.info("Database downloaded successfully.")
        except Exception as e:
            logging.error(f"Failed to download database: {e}")
            raise

    def upload_db(self, source_path):
        try:
            self.s3.upload_file(source_path, self.bucket_name, self.db_file_key)
            logging.info("Database uploaded successfully.")
        except Exception as e:
            logging.error(f"Failed to upload database: {e}")
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
