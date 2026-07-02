import re

from jobs.job import Job


def parse_linkedin(subject, snippet):
    """
    Convert a LinkedIn Job Alert email into a Job object.
    """

    company = "Unknown"

    # Example:
    # "Solutions Engineer at Hiire.co: up to $170K/year"
    match = re.search(r" at (.+?)(:|$)", subject)

    if match:
        company = match.group(1)

    salary = 0

    # Example:
    # "$170K"
    salary_match = re.search(r"\$([0-9]+)K", subject)

    if salary_match:
        salary = int(salary_match.group(1)) * 1000

    # Everything before " at " becomes the title.
    title = subject.split(" at ")[0]

    return Job(
        title=title,
        company=company,
        location="Unknown",
        salary=salary,
        source="LinkedIn"
    )