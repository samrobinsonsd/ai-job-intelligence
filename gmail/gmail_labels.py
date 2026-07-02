from gmail.gmail_client import get_gmail_service


def get_label_id(label_name):
    """
    Gets the Gmail internal ID for a label name.

    Gmail labels have display names like:
        Jobs High-Value

    But the API needs internal IDs like:
        Label_123456789
    """

    service = get_gmail_service()

    labels_response = service.users().labels().list(
        userId="me"
    ).execute()

    labels = labels_response.get("labels", [])

    for label in labels:
        if label["name"] == label_name:
            return label["id"]

    return None


def apply_label(message_id, label_name):
    """
    Applies a Gmail label to a message.
    """

    service = get_gmail_service()

    label_id = get_label_id(label_name)

    if label_id is None:
         return False



    return True

    success = apply_label(...)

    if success:
        print_success("Label applied")
    else:
        print("[-] Label not found")

    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={
            "addLabelIds": [label_id]
        }
    ).execute()

    print(f"Applied label: {label_name}")


def archive_message(message_id):
    """
    Archives a Gmail message by removing it from the inbox.

    This does not delete the message.
    It only removes the INBOX label.
    """

    service = get_gmail_service()

    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={
            "removeLabelIds": ["INBOX"]
        }
    ).execute()

    print("Archived message")