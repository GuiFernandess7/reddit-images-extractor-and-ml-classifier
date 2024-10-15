import os

from app.db.aws.db_config import S3DatabaseHandler
from app.settings.creds import BUCKET_NAME

db_filename = 'user_images.db'
local_db_path = os.path.join('app', 'data', db_filename)

with S3DatabaseHandler(BUCKET_NAME, db_filename) as s3:
    s3.download_db(local_db_path)
