import logging
from pathlib import Path

import requests


logger = logging.getLogger("ai_job_intelligence")


def fetch_job_page(url):
    """
    Fetches a job page and saves the raw HTML
    for inspection.

    Returns:
        str: Raw response HTML.
    """

    debug_directory = Path("debug")
    debug_directory.mkdir(exist_ok=True)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/150.0.0.0 "
            "Safari/537.36"
        )
    }

    logger.info(
        "FETCHING JOB PAGE | url=%s",
        url
    )

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    logger.info(
        "JOB PAGE RESPONSE | "
        "status=%s | "
        "content_length=%s | "
        "final_url=%s",
        response.status_code,
        len(response.text),
        response.url
    )

    response.raise_for_status()

    output_file = (
        debug_directory
        / "job_page.html"
    )

    output_file.write_text(
        response.text,
        encoding="utf-8"
    )

    logger.info(
        "JOB PAGE SAVED | file=%s",
        output_file
    )

    return response.text