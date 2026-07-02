import re

from bs4 import BeautifulSoup
from jobs.job import Job


def parse_salary(text):
    """
    Extracts the upper salary value from text like:
    "$130K-$170K / year"
    """

    matches = re.findall(r"\$([0-9]+)K", text)

    if matches:
        return int(matches[-1]) * 1000

    return 0


def get_clean_lines(html):
    """
    Converts raw HTML into clean visible text lines.
    """

    soup = BeautifulSoup(html, "lxml")

    lines = []

    for line in soup.get_text("\n").split("\n"):
        clean_line = line.strip()

        if clean_line and "͏" not in clean_line:
            lines.append(clean_line)

    return lines


def parse_linkedin_jobs_from_html(html):
    """
    Parses one LinkedIn job alert email and returns multiple Job objects.
    """

    lines = get_clean_lines(html)

    jobs = []

    for index, line in enumerate(lines):
        next_line = lines[index + 1] if index + 1 < len(lines) else ""
        third_line = lines[index + 2] if index + 2 < len(lines) else ""

        if "· United States" in next_line:
            title = line
            company = next_line.split("·")[0].strip()
            location = next_line.split("·")[1].strip()

            salary = 0

            if "$" in third_line:
                salary = parse_salary(third_line)

            job = Job(
                title=title,
                company=company,
                location=location,
                salary=salary,
                source="LinkedIn"
            )

            jobs.append(job)

    return jobs