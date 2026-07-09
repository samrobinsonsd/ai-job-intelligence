import logging
import re

from bs4 import BeautifulSoup
from jobs.job import Job


logger = logging.getLogger("ai_job_intelligence")


def parse_salary(text):
    """
    Extracts the upper salary value from text like:
    "$135K-$170K / year"
    """

    matches = re.findall(
        r"\$([0-9]+)K",
        text
    )

    if matches:
        return int(matches[-1]) * 1000

    return 0


def parse_company_location(text):
    """
    Parses LinkedIn company and location text.

    Example:
        "HP · Illinois, United States (Remote)"

    Returns:
        tuple: company, location
    """

    if "·" not in text:
        return "", ""

    company, location = text.split(
        "·",
        1
    )

    return (
        company.strip(),
        location.strip()
    )


def normalize_linkedin_job_url(url):
    """
    Converts a LinkedIn email tracking URL into
    a clean canonical LinkedIn job URL.

    Example:
        https://www.linkedin.com/comm/jobs/view/4437890665/?trackingId=...

    Returns:
        https://www.linkedin.com/jobs/view/4437890665/
    """

    match = re.search(
        r"/jobs/view/(\d+)",
        url
    )

    if not match:
        return url

    job_id = match.group(1)

    return (
        f"https://www.linkedin.com/"
        f"jobs/view/{job_id}/"
    )


def parse_linkedin_jobs_from_html(html):
    """
    Parses LinkedIn job cards directly from the
    email HTML DOM.

    Each LinkedIn job title anchor is used to locate
    its parent job card.
    """

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    jobs = []

    for anchor in soup.find_all(
        "a",
        href=True
    ):
        title = anchor.get_text(
            " ",
            strip=True
        )

        raw_url = anchor["href"]

        if not title:
            continue

        if "/comm/jobs/view/" not in raw_url:
            continue

        if "jobcard_body" not in raw_url:
            continue

        url = normalize_linkedin_job_url(
            raw_url
        )

        job_card = anchor.find_parent(
            "tbody"
        )

        if job_card is None:
            logger.warning(
                "JOB CARD NOT FOUND | title=%s",
                title
            )

            continue

        card_lines = [
            line.strip()
            for line in job_card.get_text(
                "\n"
            ).split("\n")
            if line.strip()
            and "͏" not in line
        ]

        if len(card_lines) < 2:
            logger.warning(
                "INVALID JOB CARD | title=%s | lines=%s",
                title,
                card_lines
            )

            continue

        company = ""
        location = ""
        salary = 0

        for line in card_lines:

            if "·" in line:
                parsed_company, parsed_location = (
                    parse_company_location(line)
                )

                if (
                    parsed_company
                    and parsed_location
                ):
                    company = parsed_company
                    location = parsed_location

            if "$" in line:
                salary = parse_salary(line)

        job = Job(
            title=title,
            company=company,
            location=location,
            salary=salary,
            source="LinkedIn",
            url=url
        )

        jobs.append(job)

        logger.info(
            "PARSED JOB | "
            "title=%s | "
            "company=%s | "
            "location=%s | "
            "salary=%s | "
            "url=%s",
            title,
            company,
            location,
            salary,
            url
        )

    logger.info(
        "Parsed %s jobs from LinkedIn email",
        len(jobs)
    )

    return jobs