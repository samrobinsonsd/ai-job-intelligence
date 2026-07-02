from gmail.gmail_client import get_gmail_service, fetch_messages
from gmail.parser import parse_linkedin
from gmail.body_extractor import extract_html

service = get_gmail_service()

messages = fetch_messages(
    query='label:Jobs',
    max_results=5
)

print(f"Found {len(messages)} messages\n")

for message in messages:

    msg = service.users().messages().get(
        userId="me",
        id=message["id"]
    ).execute()

    html = extract_html(msg)

    with open("sample_email.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("Saved sample_email.html")

    break