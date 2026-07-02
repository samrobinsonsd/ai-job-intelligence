import base64


def extract_html(msg):
    """
    Returns the HTML body from a Gmail message.

    Parameters:
        msg (dict): Gmail API message.

    Returns:
        str
    """

    payload = msg["payload"]

    if "parts" in payload:

        for part in payload["parts"]:

            if part["mimeType"] == "text/html":

                data = part["body"]["data"]

                return base64.urlsafe_b64decode(
                    data
                ).decode("utf-8")

    return ""