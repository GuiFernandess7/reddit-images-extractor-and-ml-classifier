import requests
from datetime import datetime, timezone
import logging

from app.settings.creds import (
    USER_AGENT,
    INITIAL_PARAMS,
    BUCKET_NAME,
)

from app.errors.errors import *
from app.api.token import get_token_access
from app.db.entities.UserImages import UserImages
from app.db.aws.db_config import S3DatabaseHandler
from app.db.config.db_config import DBConnectionHandler

def set_request_headers(user_agent) -> dict:
    """Set the request headers by getting the access token."""
    headers = {'User-Agent': user_agent}
    try:
        token = get_token_access(headers=headers, params=INITIAL_PARAMS)
    except RequestError as e:
        raise RequestError(f"{e}") from e
    except APITokenError as e:
        raise APITokenError(f"{e}") from e
    headers['Authorization'] = f'bearer {token}'
    return headers

def get_subreddit_response(subreddit, headers):
    """Does the GET request to reddit"""
    url = f'https://oauth.reddit.com/r/{subreddit}/new?limit=100'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise SubredditPostsError(f"Error retrieving posts: {response.status_code} - {response.text}")

    return response.json()

def extract_images_from_response(response) -> list:
    """Extract the images urls from the api response"""
    gallery_items = response['data']['children']
    imgs_link = []

    for post in gallery_items:
        user_imgs = post['data']
        created_ts = user_imgs['created']
        created_date = datetime.fromtimestamp(created_ts, tz=timezone.utc)

        if user_imgs.get('gallery_data') is not None:
            img_id = user_imgs['gallery_data']['items'][0]['media_id']
            img_url = f'https://i.redd.it/{img_id}.jpg'

            imgs_link.append(UserImages(
                ts=created_ts,
                image_url=img_url,
                created_at=created_date,
                sex=None
                )
            )

    return imgs_link

def find_new_data(session, images) -> list:
    """Returns a list of new images that are not already in the database."""
    existing_timestamps = {image.ts for image in session.query(UserImages.ts).all()}
    return [image for image in images if image.ts not in existing_timestamps]

def insert_data_to_sqlite(session, new_posts) -> None:
    """Inserts new posts into the SQLite database."""
    if not new_posts:
        logging.info("No new posts to insert.")
        return

    try:
        session.add_all(new_posts)
        session.commit()
        logging.info(f"POSTS SENT: {len(new_posts)}")
    except Exception as e:
        session.rollback()
        raise DatabaseInsertError(f"[DatabaseInsertError]: {e}") from e

def main():
    subreddit = 'amiugly'
    db_filename = 'user_images.db'
    local_db_path = 'app/data/user_images.db'
    headers = set_request_headers(USER_AGENT)

    response = get_subreddit_response(subreddit, headers)
    images = extract_images_from_response(response)
    logging.info(f"{len(images)} post images found.")

    with S3DatabaseHandler(BUCKET_NAME, db_filename) as s3:
        s3.download_db(local_db_path)

        with DBConnectionHandler() as db_handler:
            new_posts = find_new_data(db_handler, images)
            if new_posts:
                insert_data_to_sqlite(db_handler, images)
                s3.upload_db(local_db_path)
            else:
                logging.info("No new posts found, skipping S3 upload.")

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] - [%(levelname)s] - %(message)s'
    )
    logger = logging.getLogger(__name__)
    main()
