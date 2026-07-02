import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# MODIFY Gmail access.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify"
]


def get_gmail_service():
    """
    Authenticates with Gmail and returns an authenticated
    Gmail API service object.
    """

    creds = None

    # Reuse saved login session if it exists.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    # Login if needed.
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        # Save credentials for future runs.
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build(
        "gmail",
        "v1",
        credentials=creds
    )

def fetch_messages(query="label:job", max_results=10):
    """
    Fetches Gmail messages matching a Gmail search query.

    Parameters:
        query (str): Gmail search query.
        max_results (int): Maximum number of emails to retrieve.

    Returns:
        list
    """

    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        q=query,
        maxResults=max_results
    ).execute()

    return results.get("messages", [])