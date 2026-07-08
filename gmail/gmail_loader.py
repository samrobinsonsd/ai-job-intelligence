from gmail.gmail_client import get_gmail_service, fetch_messages
from gmail.body_extractor import extract_html
from gmail.html_parser import parse_linkedin_jobs_from_html


def load_jobs_from_gmail(query='label:Jobs', max_results=10):
    """
    Loads Gmail job alert messages and converts them into Job objects.

    Parameters:
        query (str): Gmail search query.
        max_results (int): Maximum number of messages to process.

    Returns:
        list[Job]: Job objects parsed from Gmail messages.
    """

    service = get_gmail_service()

    messages = fetch_messages(
        query=query,
        max_results=max_results
    )

    jobs = []
    
    for message in messages:
        msg = service.users().messages().get(
            userId="me",
            id=message["id"]
        ).execute()

        # Extract HTML from the Gmail message.
        html = extract_html(msg)

        # Parse multiple jobs from this one LinkedIn email.
        parsed_jobs = parse_linkedin_jobs_from_html(html)

        # Attach the original Gmail message ID to every Job object.
        # This lets us apply Gmail labels later.
        for job in parsed_jobs:
            job.message_id = message["id"]

        # Add all parsed jobs to the master jobs list.
        jobs.extend(parsed_jobs)

    return jobs