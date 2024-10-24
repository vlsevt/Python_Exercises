"""Appi."""
import os.path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
RANGE = 'A:A'


def get_links_from_spreadsheet(id: str, token_file_name: str):
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    credential = Credentials.from_authorized_user_file(token_file_name, SCOPES) if os.path.exists('token.json') else None

    try:
        service = build('sheets', 'v4', credentials=credential)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id, range=RANGE).execute()
        values = []

        if not result['values']:
            return 'The spreadsheet is empty'

        for element in result['values']:
            values += element

        return values

    except HttpError as err:
        return err


if __name__ == "__main__":
    get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')
