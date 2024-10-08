import dotenv
import os
dotenv.load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
USER_AGENT = os.getenv('USER_AGENT')
BUCKET_NAME = 'reddit-images-bucket'
DB_FILE_KEY = 'user_images.db'
LOCAL_DB_PATH = 'app/data/user_images.db'

INITIAL_PARAMS = {
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD
}