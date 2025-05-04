import os
import logging
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


class GoogleDriveDatabaseHandler:
    def __init__(self, credentials_file, folder_id=None):
        self.credentials = self._authenticate(credentials_file)
        self.drive_service = build("drive", "v3", credentials=self.credentials)
        self.folder_id = folder_id

    def _authenticate(self, credentials_file):
        """Autentica com o Google Drive usando um arquivo de credenciais."""
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file(
                "token.json", ["https://www.googleapis.com/auth/drive.file"]
            )

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                creds = Credentials.from_service_account_file(
                    credentials_file,
                    scopes=["https://www.googleapis.com/auth/drive.file"],
                )

            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return creds

    def download_db(self, dest_path):
        """Baixa o arquivo do Google Drive para o destino especificado."""
        try:
            file_id = self._get_file_id()
            request = self.drive_service.files().get_media(fileId=file_id)
            fh = open(dest_path, "wb")
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            logging.info("Database downloaded successfully.")
        except Exception as e:
            logging.error(f"Failed to download database: {e}")
            raise

    def upload_db(self, source_path):
        """Faz upload de um arquivo para o Google Drive."""
        try:
            file_metadata = {
                "name": os.path.basename(source_path),
                "parents": [self.folder_id] if self.folder_id else [],
            }
            media = MediaFileUpload(source_path, resumable=True)
            file = (
                self.drive_service.files()
                .create(body=file_metadata, media_body=media, fields="id")
                .execute()
            )
            logging.info(f"Database uploaded successfully, file ID: {file.get('id')}")
        except Exception as e:
            logging.error(f"Failed to upload database: {e}")
            raise

    def _get_file_id(self):
        """Obtém o ID do arquivo armazenado no Google Drive."""
        if not self.folder_id:
            # Caso não tenha um folder_id, busca pelo arquivo mais recente
            results = (
                self.drive_service.files()
                .list(q="name='user_images.db'", fields="files(id)")
                .execute()
            )
            items = results.get("files", [])
            if not items:
                logging.error("No file found in Google Drive.")
                raise Exception("No file found")
            file_id = items[0]["id"]
        else:
            # Busca o arquivo dentro de uma pasta específica
            query = f"'{self.folder_id}' in parents and name='user_images.db'"
            results = (
                self.drive_service.files().list(q=query, fields="files(id)").execute()
            )
            items = results.get("files", [])
            if not items:
                logging.error("No file found in the specified folder.")
                raise Exception("No file found in the specified folder")
            file_id = items[0]["id"]

        return file_id

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
